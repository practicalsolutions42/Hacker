import json
from urllib.request import urlopen
from tabulate import tabulate

url = "https://ipinfo.io/json"
response = urlopen(url)
data = json.load(response)

table = [["IP-Adress:",data["ip"]],
         ["Server:",   data["org"]],
         ["Şehir:",    data["city"]],
         ["Ülke:",     data["country"]],
         ["Bölge:",    data["region"]],
         ["Lokasyon:", data["loc"]],
         ["Posta Kodu:",data["postal"]],
         ["Zaman Dilimi:",data["timezone"]]]

print("response dönüşü")
print(tabulate(table))