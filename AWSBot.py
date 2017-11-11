import json
import requests
import subprocess
import argparse


class botCli(object):

    def __init__(self,path,url,token,profile):
        self.path = path
        self.url= url.format(token)
        self.profile=profile

    def get_url(self,url):
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content

    def send_message(self,text, chat_id):
        url = self.url + "sendMessage?text={}&chat_id={}".format(text, chat_id)
        self.get_url(url)

    def get_json_from_url(self,url):
        content = self.get_url(url)
        js = json.loads(content)
        return js

    def get_updates(self):
        url = self.url + "getUpdates?timeout=5"
        js = self.get_json_from_url(url)
        return js

    def get_last_chat_id_and_text(self,updates):
        num_updates = len(updates["result"])
        last_update = num_updates - 1
        text = updates["result"][last_update]["message"]["text"]
        chat_id = updates["result"][last_update]["message"]["chat"]["id"]
        m_id = updates["result"][last_update]["update_id"]

        return (chat_id,text,m_id)

    def execute_analysis_aws(self,chat_id):
        cmd =[self.path, "-p",self.profile,"-M","mono"]
        p = subprocess.Popen(cmd,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

        for line in iter(p.stdout.readline, b''):
            print(line.decode('utf-8'))
            self.send_message(line.decode('utf-8'),chat_id)

    def execute_nmap(self,chat_id,args):
        cmd = ["nmap"]
        args.pop(0)

        for i in args:
            cmd.append(i)
        print(cmd)

        p = subprocess.Popen(cmd,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

        for line in iter(p.stdout.readline, b''):
            print(line.decode('utf-8'))
            self.send_message(line.decode('utf-8'),chat_id)

    def get_initID(self):
        _, _, init_update = self.get_last_chat_id_and_text(self.get_updates())
        return init_update

    def run(self,chat_id):
        last_id = self.get_initID()
        print("[*][*][*][*][*] Running Telegram Server Bot ... [*][*][*][*][*]")
        while True:
            user_id, msg, current_id = self.get_last_chat_id_and_text(self.get_updates())
            if user_id in chat_id and current_id > last_id:
                last_id = current_id
                if msg == "/RunAnalysis":
                    self.execute_analysis_aws(user_id)
                if msg.split(' ', 1)[0] == "/Nmap":
                    self.execute_nmap(user_id,msg.split())
                else:
                    self.send_message("To scan your AWS Account use /RunAnalysis, to scan another network could use /Nmap",user_id)

if __name__ == '__main__':
    #Arguments
    parser = argparse.ArgumentParser(description='[+][+] Telegram Bot Server to audit CIS AWS Security Checks')
    parser.add_argument('--token','-t', type=str, required=True ,help='Token API Telegram Bot')
    parser.add_argument('--path',"-p", type=str,  required=True, help='Prowler Path')
    parser.add_argument('--awsprofile',"-a", type=str,  required=True, help='Profile AWS previously configured with \"aws configure\"')
    parser.add_argument('--users', '-u',type=int ,required=True , nargs='+', help='Users allowed')

    args = parser.parse_args()

    url = "https://api.telegram.org/bot{}/"

    #Create de cli
    botcli = botCli(args.path,url,args.token,args.awsprofile)
    last_id =botcli.get_initID()

    #Your ID's user
    chat_id=args.users
    botcli.run(chat_id)


