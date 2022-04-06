import requests, time, json

s = requests.Session()
accounts=[
    #["username","password"],
    #["username","password"]


]

def main():
    for account in accounts:
        checkin(account[0], account[1])

def checkin(username, password):

    print(username)

    login_url = "https://w1.v2free.net/auth/login"
    headers1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0",
        "Referer": "https://w1.v2free.net/auth/login",
        }
    data1 = {
        "email":username,
        "passwd":password,
        "code":"",
        }
    r1 = s.post(login_url, data=data1, headers=headers1, timeout=5)
    print(r1.json().get("msg"))

    time.sleep(7)

    target_url = "https://w1.v2free.net/user/checkin"
    headers2 = {
        "Host": "w1.v2free.net",
        "Content-Length":"0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0",
        "Referer": "https://w1.v2free.net/user",
        "Accept-Encoding": "gzip, deflate, br",
    }
    r2 = s.post(target_url, headers=headers2, timeout=5)
    print(r2.json().get("msg"))

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(e.args)
