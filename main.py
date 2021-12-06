import requests
import re
from bs4 import BeautifulSoup
import pymongo
import redis
import time

r = redis.Redis()

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["Bitcoin"]
#mycol = mydb["Transactions"]

wait = time.sleep

# f =  open('bitcoin.txt', 'w+')

def scraper():
    # The Code
    url = requests.get(f'https://www.blockchain.com/btc/unconfirmed-transactions')
    soup = BeautifulSoup(url.text, 'html.parser')
    html_tag = soup.find_all('div', {"class": "sc-1g6z4xm-0 hXyplo"})

    items_list = []
    for item in html_tag:
        items = (item.get_text())
        items_list.append(items)

    items_list1 = []
    for item in items_list:
        i = item.replace('Time', ' ')
        items_list1.append(i)

    items_list2 = []
    for item in items_list1:
        i = re.sub('Hash|Time|Amount|BTCAmount|(BTC)|(USD)|[()]', '', item)
        items_list2.append(i)


    items_list3 = []
    for item in items_list2:
        i = item.split(" ")
        items_list3.append(i)

    sorted_list = sorted(items_list3, key=lambda x: float(x[2]),reverse=True)

    Hash = sorted_list[0][0]
    Time = sorted_list[0][1]
    BTC = sorted_list[0][2]
    USD = sorted_list[0][4]

    # Print on the txt file
    # with open('bitcoin.txt', 'a+') as f:

    # f.write('Hash: '+ item[0] + "\n")
    # f.write('Time: ' + item[1] + "\n")
    # f.write('Amount(BTC): ' + item[2] + "\n")
    # f.write('Amount(USD): ' + item[4] + "\n\n")

    # Print on the console
    print('Hash: ' + Hash)
    print('Time: ' + Time)
    print('Amount(BTC): ' + BTC)
    print('Amount(USD): ' + USD + "\n")

    # MONGO
    #mydict = {"Hash": Hash, "Time": Time, "Amount(BTC)": BTC, "Amount(USD)": USD}
    #x = mycol.insert_one(mydict)

    # REDIS
    for item in sorted_list:
        Hash = item[0]
        Time = item[1]
        BTC = item[2]
        USD = item[4]

        r.hset(Hash, "Time", Time)
        r.hset(Hash, "BTC", BTC)
        r.hset(Hash, "USD", USD)


    wait(60)

    for key in r.scan_iter("*"):
        r.delete(key)



index = 1
while index < 20:
    scraper()
    index = index + 1

