# -*- coding: utf-8 -*-
"""
cron: 55 7 * * *
new Env('恩山论坛');
"""

import os
import requests, re, traceback, sys
from io import StringIO

from notify import send

class EnShan:
    def __init__(self, cookie):
        self.sio = StringIO()
        self.Cookies = cookie
        self.cookie = ''

    def sign(self):
        url = "https://www.right.com.cn/FORUM/home.php?mod=spacecp&ac=credit&showcredit=1"
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
            'Cookie': self.cookie
        }
        res = requests.get(url, headers=headers)
        if '登录' in res.text:
            print("Cookie失效")
            self.sio.write("Cookie失效\n")
        else:
            coin = re.findall("恩山币: </em>(.*?)nb &nbsp;", res.text)[0]
            print(f"签到成功, 剩余{coin}nb")
            self.sio.write(f"签到成功, 剩余{coin}nb\n")

    def SignIn(self):
        print("【恩山论坛 日志】")
        self.sio.write("【恩山论坛】\n")
        for cookie in self.Cookies:
            cookie = cookie.get("user")
            print(f"{cookie.get('name')} 开始签到...")
            self.sio.write(f"{cookie.get('name')}: ")
            self.cookie = cookie.get('cookie')
            try:
                self.sign()
            except:
                print(f"{cookie.get('name')}: 异常 {traceback.format_exc()}")
                if '签到存在异常, 请自行查看签到日志' not in self.sio.getvalue():
                    self.sio.write('签到存在异常, 请自行查看签到日志\n')
        return self.sio

if __name__ == '__main__':
  Cookies = os.getenv("ENSHAN_COOKIE")
  if Cookies != None:
    Cookies = json.loads(Cookies)
    enshan = EnShan(Cookies)
    sio = enshan.SignIn()
    print(f'\n{sio.getvalue()}')
    send('恩山论坛', sio.getvalue())
