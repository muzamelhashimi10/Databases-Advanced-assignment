# Scraper-Assignment 1

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
We use anaconda, pycharm, simple python file or whatever for our editor.
We use terminal to execute the the code
first we need to get to the correct folder
for example: cd Desktop/scraper

Once we are in the correct folder, we just type in python3 scraper.py
An the code will be executed.

And you will notice that a bitcoin file has been created in the scraper folder where the values get stored in each minute. 
To keep along with each append to the bitcoin file. I printed the values at the same time while the append happens.

# Mongo-Assignment 2

## What we have to do?
In the previous exercise, we made the first version of our scraper. However, we simply wrote out our output to a logfile. This is far off from the ideal. Seeing as we now know how to use Mongo DB, we will put this knowledge into practice.

For this assignment, you will improve your project by doing the following:

1. Make a Bash Script which sets up a Mongo DB Server locally on your virtual machine. Configure this database for the storage of the Bitcoin data.
2. Adapt your Scraper such that it stores each observation which you wish to store (each minute) is saved into a JSON document in the Mongo DB you configured in 1.
3. Optionally, if you did not manage to make your scraper realtime yet, include a Bash script now which runs the scraper every minute.

## Libraries needed
import pymongo

we need to run pip install pymongo probably on the terminal on our virutal machine if it is not installed before.

## Explaining the code
A simple while loop is used to scrape the values each 60 seconds upto 10 values. And then it is saved in the mongo database.
so we append the most valuable transaction each 60 seconds.

## Running it on the virtual machine
Steps to install mongodb:
1. wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
2. sudo apt-get install gnupg
3. wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
4. echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
5. sudo apt-get install -y mongodb-org
6. ps --no-headers -o comm 1

To start our mongodb, we run first:
sudo systemctl start mongod
To check the status:
sudo systemctl status mongod

Steps to install mongodb compass:
1. wget https://downloads.mongodb.com/compass/mongodb-compass_1.26.1_amd64.deb
2. sudo dpkg -i mongodb-compass_1.26.1_amd64.deb

We use anaconda, pycharm, simple python file or whatever for our editor.
We use terminal to execute the the code
first we need to get to the correct folder
for example: cd Desktop

Once we are in the correct folder, we just type in python3 scraper.py to run it
An the code will be executed.

And you will notice that in our mongodb compass that a new database by the name of bitcoin has created and if you refresh each 60 seconds a new transaction is added. 
To keep along with each append to the bitcoin database. I printed the values at the same time while the append happens.

# REDIS-Assignment 3

## What we have to do?
We have to make two scripts-Redis and mongo
We use redis as a caching mechanism so the whole thing gets stored in redis first and then gets cleared after a minute. 
We use Mongo to get data from redis to our mongodb.

## Libraries needed
import redis
import mongo

we need to run pip install redis if not previously installed

## Explaining the code
Just a simple caching mechanism where the datas are stored in for a minute and then it gets cleared and the new datas coming in. We use redis becuase it is fast.

## Running it on the virtual machine
Steps to install redis:
1. wget http :// download.redis.io/redis -stable.tar.gz
2. tar xvzf redis -stable.tar.gz
3. cd redis -stable
4. make
5. make test

To start our redis:
1. cd src
2. redis-server
3. redis-cli ping

if PONG appears it means we are good to go

To help you see what are you doing, we install redis GUI:

Steps to install redis GUI(It is useful to see the process of adding to the redis and deleting from the redis:

sudo snap install redis-gui

We use anaconda, pycharm, simple python file or whatever for our editor.
We use terminal to execute the the code
first we need to get to the correct folder
for example: cd Desktop

Once we are in the correct folder, we just type in python3 main.py to run it
An the code will be executed.
All the transactions are saved in redis and each minute replaced by new transactions.

And you will notice that in our redis GUI the whole data gets stored in and if you refresh after 1 minute, you will notice the previous datas are deleted and new data have appeared. 

Then we run python3 mongo.py, so the transactions that are stored in redis we get them to the mongodb.

So we add the the transactons that are in our redis, we send them to our mongodb on a new database called Bitcoin.

# Final-Assignment 4

## What we have to do?
Get Docker up and running on the VM. Search for a docker image for Redis and for Mongo on Docker Hub.
Get these up and running, and try to connect your scraper to them. Upload the scripts you have used for this, and a screenshot with it working to Canvas.

## What we have to do before running connecting to the scraper?
Install docker from docker.com/get-started
Install docker image for redis and for mongo by running 
docker pull redis and docker pull mongo 

After getting redis and mongo images. we build a docker container file for our scrapers.
We use the command,
For redis scraper:
docker build -t python-redis .  
For mongo scraper:
docker build -t python-mongo . 

## Running it on the virtual machine

After building our scraper containers, we try to connect them with the corresponding images. python-redis with redis image and python-mongo with mongo image.
By running command,
For redis,
first: docker run -d --network=host redis
Second: docker run --network=host python-redis
To run redis, 
redis-cli then PING if PONG(means redis is running)

We do the same with for mongo,
irst: docker run -d --network=host mongo
Second: docker run --network=host python-mongo
We should always start mongo so the mongo docker could work:
sudo sytemctl start mongod

How to run docker?
sudo systemctl restart docker
If sometime docker shows connection error. It can be solved through:
sudo chmod 666 /var/run/docker.sock


### Some useful commands for docker
docker ps (shows all the running containers)
docker ps -a (shows all the container whether running or stopped)
docker info
docker image ls (list of all images installed)





