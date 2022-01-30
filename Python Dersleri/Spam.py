import time

import requests

proxy = {"https":"https://scraperapi:a0cc1efd13b358460567421afab688a9@proxy-server.scraperapi.com:8001"}

while True:
    time.sleep(1)
    r= requests.get("https://httpbin.org/ip",proxies=proxy,verify=False)
    print(r.text)