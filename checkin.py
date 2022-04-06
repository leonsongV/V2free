import requests, time, json

s = requests.Session()





def main():
    try:
        print(username)
        login(username, password)
        time.sleep(7)
        checkin()
    except Exception as e:
        print(e.args)

def login(username, password):
    url = "https://w1.v2free.net/auth/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0",
        "Referer": "https://w1.v2free.net/auth/login",
        }
    data = {
        "email":username,
        "passwd":password,
        "code":"",
        }
    r = s.post(url, data=data, headers=headers, timeout=5)
    print(r.json().get("msg"))
    return s

def checkin():
    url = "https://w1.v2free.net/user/checkin"
    headers = {
        "Host": "w1.v2free.net",
        "Content-Length":"0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0",
        "Referer": "https://w1.v2free.net/user",
        "Accept-Encoding": "gzip, deflate, br",
    }
    r = s.post(url, headers=headers, timeout=5)
    print(r.json().get("msg"))
if __name__ == "__main__":
    main()