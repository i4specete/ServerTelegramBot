# CloudBot to monitoring your AWS Account or others nertworks/services

## Introduction

CloudBot to scan your AWS Account with the tool Prowler https://github.com/Alfresco/prowler, which aplies CIS Security Controls in your AWS Account. Also, you can use Nmap command remotely from your phone.

## Requirements

First of all, you need to have installed:

 - Create a Telegram Bot with @BotFather
 - awscli https://github.com/aws/aws-cli and use "aws configure" to create a profile.
 - Install nmap https://nmap.org/
 - prowler https://github.com/Alfresco/prowler

To run the server:

- pip3 install -r requirements.txt
- python3.6 CloudBot.py



usage: CloudBot.py [-h] --token TOKEN --path PATH --users USERS [USERS ...] 

[+][+] Telegram Bot Server to audit CIS AWS Security Checks

   -h, --help     show this help message and exit

  --token TOKEN, -t TOKEN   Token API Telegram Bot

  --path PATH, -p PATH  Prowler Path

  --users USERS [USERS ...], -u USERS [USERS ...]
                        Users allowed

Ex: id":7390313", you can find out this ID in your Telegram Bot API:
https://api.telegram.org/bot{}/getUpdates




## Examples

Example:

python CloudBot.py -t 4kjnfjdhahjfadf62627288373 -p "./prowler" -u 73903 7950749 72378932083 

Search the bot previously created. Torun the scan from your Telegram Account you have to send de command "/ScanAWS -p {profile}"

![Telegram](https://i.imgur.com/8Wej4bL.png)

![Telegram](https://i.imgur.com/TePXVyP.jpg)


Example: /Nmap 
![Telegram](https://i.imgur.com/5FCy9xh.png)


# CloudBot Dockerized

## Telegram Bot

> Create the bot with BotFather

> Take the TOKEN API Telegram Bot.

> Extract your ID with the following URL: 

`https://api.telegram.org/bot{TOKEN}/getUpdates` 

> The ID is the json `id:`


## Install AWS CLI in the Host that run Docker

`sudo apt-get install aws-cli`


## Write Amazon API Key and Secret

`aws configure`


## Copy credentials File to repository

`mkdir CloudBot`

`cd CloudBot`

`cp ~/.aws/credentials .`

## Add to .gitignore credentials File

`# Credentials AWS

credentials`


## Build Container

`sudo docker build -t cloudbot .`


## Run and Lauch Interactive Shell

`sudo docker run -ti cloudbot /bin/bash`


## Execution
`sudo docker run cloudbot python /CloudBot/ServerTelegramBot/CloudBot.py -t xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Ls -p ./CloudBot/prowler/prowler -u xxxxxxxxx`


## Execution from Telegram
`/ScanAWS -p default`





## To do:

- Add more hacking tools to conquer the world
- Add module to parse the output of diferents tools
- Refactor and reestructure the code 






