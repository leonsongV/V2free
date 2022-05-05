import requests, json, argparse
import os
from sendNotify import send

class CheckIn(object):
    client = requests.Session()
    login_url = "https://w1.v2free.net/auth/login"
    sign_url = "https://w1.v2free.net/user/checkin"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_in(self):
        self.login()
        headers = {
            "Host": "w1.v2free.net",
            "Content-Length": "0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0",
            "Referer": "https://w1.v2free.net/user",
            "Accept-Encoding": "gzip, deflate, br",
        }
        response = self.client.post(self.sign_url, headers=headers, timeout=5)
        print(response.json()["msg"])

    def login(self):
        print(self.username)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0",
            "Referer": "https://w1.v2free.net/auth/login",
            }
        data = {
            "email": self.username,
            "passwd": self.password,
            "code": "",
            }
        response = self.client.post(self.login_url, data=data, headers=headers, timeout=5)
        print(response.json()["msg"])
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='V2ray签到脚本')
    parser.add_argument('--username', type=str, help='账号')
    parser.add_argument('--password', type=str, help='密码')
    args = parser.parse_args()
    helper = CheckIn(args.username, args.password)
    res = helper.check_in()
    send('V2free', res)

 
