# CloudBot Dockerized

### Telegram Bot

> Create the bot with BotFather

> Take the TOKEN API Telegram Bot.

> Extract your ID with the following URL: 

`https://api.telegram.org/bot{TOKEN}/getUpdates` 

> The ID is the json `id:`


### Install AWS CLI in the Host that run Docker

`sudo apt-get install aws-cli`


### Write Amazon API Key and Secret

`aws configure`


### Copy credentials File to repository

`mkdir CloudBot`

`cd CloudBot`

`cp ~/.aws/credentials .`

### Add to .gitignore credentials File

`# Credentials AWS

credentials`


### Build Container

`sudo docker build -t cloudbot .`


### Run and Lauch Interactive Shell

`sudo docker run -ti cloudbot /bin/bash`


### Execution
`sudo docker run cloudbot python /CloudBot/ServerTelegramBot/CloudBot.py -t xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Ls -p ./CloudBot/prowler/prowler -u xxxxxxxxx`


### Execution from Telegram
`/ScanAWS -p default`