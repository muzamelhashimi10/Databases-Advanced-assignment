# Scraper-Assignment

## What we have to do?
Get a new Ubuntu Virtual Machine up and running on your own machine. Install Python 3 on this VM, and make a Web Scraper on this VM.

Bitcoin, and cryptocurrencies in general, are one of the more interesting technological aspects of our time. For Data Managers like us, the interesting part lies in that all Bitcoin data is publicly available (be it encrypted). We won't go into the technicalities of Bitcoin here, but simply try to do something with the loads of data it produces.

You will make a Scraper which outputs the most valuable Hash for Bitcoin per minute. The page you will scrape is: https://www.blockchain.com/btc/unconfirmed-transactions (Links to an external site.)
First of all, you clearly see that the data on this website is updated in realtime! This is the interesting aspect you should work with. Next, you see lots of observations with the same variables. The variables are: 

.Hash
.Time
.Amount (BTC)
.Amount (USD)

## Libraries needed
import requests
import re
from bs4 import BeautifulSoup
from time import time, sleep

we need to run pip install bs4 probably on the terminal on our virutal machine if it is not installed before.
The other libraries are there already.

## Explaining the code
A simple while loop is used to scrape the values each 60 seconds upto 10 values. And then it is saved in a log file called bitcoin.txt.
so we append the most valuable transaction each 60 seconds.

## Running it on the virtual machine
Steps to install mongodb:
1. wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
2. sudo apt-get install gnupg
3. wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
4. echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
5. sudo apt-get install -y mongodb-org
6. ps --no-headers -o comm 1
7. sudo systemctl start mongod
To check the status:
sudo systemctl status mongod

We use anaconda, pycharm, simple python file or whatever for our editor.
We use terminal to execute the the code
first we need to get to the correct folder
for example: cd Desktop/scraper

Once we are in the correct folder, we just type in python3 scraper.py
An the code will be executed.

And you will notice that a bitcoin file has been created in the scraper folder where the values get stored in each minute. 
To keep along with each append to the bitcoin file. I printed the values at the same time while the append happens.
voila!

