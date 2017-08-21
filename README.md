# [MailFail](https://sploit.io/2017/08/21/mailfail-a-story-of-scary-newsletters-and-evil-signup-forms/) 
#### Utilize misconfigured newsletter forms to spam / deny service to an inbox
This is a very minimal PoC which uses public data and simple Python3 programming to show how serious / easy to perform email signup automation abuse can be.

>This tool is only for academic purposes and testing under controlled 
environments. Do not use without obtaining proper authorization from 
the network owner of the network under testing. The author bears no
responsibility for any misuse of the tool. __This PoC is as reliable
as the example websites, it does not have a permanent lifespan.__
 
![example](https://sploit.io/mailfail.gif)

## Requirements
* Python3
* pip3
* tor (not necessary but recommended)

## Dependencies
colorama==0.3.9
urllib3==1.21.1

## Install (tested Windows & Linux)
``git clone https://github.com/m0rtem/MailFail.git``

``cd MailFail``

``sudo pip3 install -r requirements.txt``

``python3 mailfail.py --target some@example.com --tor``

Will run a email spam campaign on ``some@example.com`` using the Tor network to mask requests.

``python3 mailfail.py -h``

For help.
