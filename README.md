# Telegram Bot Server to monitoring your AWS Account 

## Introduction

Telegram Bot Server to scan your AWS Account with the tool Prowler https://github.com/Alfresco/prowler, which aplies CIS Security Controls in your AWS Account.

## Requirements

First of all, you need to have installed:
 - Create a Telegram Bot with @BotFather
 - awscli https://github.com/aws/aws-cli and use "aws configure" to create a profile.
 - prowler https://github.com/Alfresco/prowler

  
usage: bot.py [-h] --token TOKEN --path PATH --users USERS [USERS ...]

[+][+] Telegram Bot Server to audit CIS AWS Security Checks

   -h, --help     show this help message and exit

  -- token TOKEN, -t TOKEN   Token API Telegram Bot


  --path PATH, -p PATH  Prowler Path

  --awsprofile AWSPROFILE, -a AWSPROFILE
                        Profile AWS previously configured with "aws configure"

  --users USERS [USERS ...], -u USERS [USERS ...]
                        Users allowed

Ex: id":7390313", you can find out this ID in your Telegram Bot API:
https://api.telegram.org/bot{}/getUpdates




## Examples

Example:

python AWSbot.py -t 4kjnfjdhahjfadf62627288373 -p "./prowler" -u 73903 7950749 72378932083 -a default


