import requests
import re
from bs4 import BeautifulSoup
from time import time, sleep
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Bitcoin"]
mycol = mydb["Transactions"]


# f =  open('bitcoin.txt', 'w+')
index = 0

while (index < 10):
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
    index = index + 1

    # with open('bitcoin.txt', 'a+') as f:
    for item in sorted_list[:1]:
        #f.write('Hash: '+ item[0] + "\n")
        print('Hash: '+ item[0])
        mydict = {"Hash": item[0], "Time": item[1], "Amount(BTC)": item[2], "Amount(USD)": item[4]}

        x = mycol.insert_one(mydict)
         #f.write('Time: ' + item[1] + "\n")
        print('Time: ' + item[1])
        #f.write('Amount(BTC): ' + item[2] + "\n")
        print('Amount(BTC): ' + item[2])
        #f.write('Amount(USD): ' + item[4] + "\n\n")
        print('Amount(USD): ' + item[4] + "\n")
        sleep(60 - time() % 60)


