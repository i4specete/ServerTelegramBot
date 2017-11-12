# Telegram Bot Server to monitoring your AWS Account or others nertworks/services

## Introduction

Telegram Bot Server to scan your AWS Account with the tool Prowler https://github.com/Alfresco/prowler, which aplies CIS Security Controls in your AWS Account. Also, you can use Nmap command remotely from your phone.

## Requirements

First of all, you need to have installed:

 - Create a Telegram Bot with @BotFather
 - awscli https://github.com/aws/aws-cli and use "aws configure" to create a profile.
 - Install nmap https://nmap.org/
 - prowler https://github.com/Alfresco/prowler

To run the server:

- pip3 install -r requirements.txt
- python3.6 AWSBot.py



usage: bot.py [-h] --token TOKEN --path PATH --users USERS [USERS ...] 

[+][+] Telegram Bot Server to audit CIS AWS Security Checks

   -h, --help     show this help message and exit

  -- token TOKEN, -t TOKEN   Token API Telegram Bot

  --path PATH, -p PATH  Prowler Path

  --users USERS [USERS ...], -u USERS [USERS ...]
                        Users allowed

Ex: id":7390313", you can find out this ID in your Telegram Bot API:
https://api.telegram.org/bot{}/getUpdates




## Examples

Example:

python AWSbot.py -t 4kjnfjdhahjfadf62627288373 -p "./prowler" -u 73903 7950749 72378932083 

Search the bot previously created. Torun the scan from your Telegram Account you have to send de command "/ScanAWS -p {profile}"

![Telegram](https://i.imgur.com/8Wej4bL.png)

![Telegram](https://i.imgur.com/TePXVyP.jpg)


Example: /Nmap 
![Telegram](https://i.imgur.com/5FCy9xh.png)

## To do:

- Add more hacking tools to conquer the world
- Add module to parse the output of diferents tools
- Refactor and reestructure the code 






