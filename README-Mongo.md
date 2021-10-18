# Mongo-Assignment

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
A simple while loop is used to scrape the values each 60 seconds upto 10 values. And then it is saved in mongo database.
so we append the most valuable transaction each 60 seconds.

## Running it on the virtual machine
We use anaconda, pycharm, simple python file or whatever for our editor.
We use terminal to execute the the code
first we need to get to the correct folder
for example: cd Desktop/scraper

Once we are in the correct folder, we just type in python3 mongo.py to run it
An the code will be executed.

And you will notice that in our mongo database a new database by the name of bitcoin has created and if you refresh each 60 seconds a new transaction is added. 
To keep along with each append to the bitcoin database. I printed the values at the same time while the append happens.
voila!
