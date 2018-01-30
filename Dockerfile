# CloudBot.py Dockerized
FROM python:3@sha256:98149ed5f37f48ea3fad26ae6c0042dd2b08228d58edc95ef0fce35f1b3d9e9f

MAINTAINER kxuan.celtik@gmail.com: 0.1

RUN apt-get update \
    && apt-get install -y nmap awscli git \
    && mkdir /CloudBot && cd /CloudBot \
    && git clone https://github.com/Alfresco/prowler /CloudBot/prowler \
    && git clone https://github.com/i4specete/ServerTelegramBot.git /CloudBot/ServerTelegramBot \
    && cd /CloudBot/ServerTelegramBot \
    && pip3 install -r requirements.txt \
    && cd /CloudBot

RUN mkdir /root/.aws

ADD credentials /root/.aws/

CMD ["python /CloudBot/ServerTelegramBot/CloudBot.py"]






