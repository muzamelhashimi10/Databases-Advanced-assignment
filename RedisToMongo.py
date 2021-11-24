import redis
import pymongo

r = redis.Redis()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Bitcoin"]
mycol = mydb["Transactions"]

for key in r.keys(pattern="*"):
    Hash = key
    BTC = float(r.hvals(key)[0])
    Time = str(r.hvals(key)[1])
    USD = float(r.hvals(key)[2])
    mydict = {"Hash": Hash, "Time": Time, "Amount(BTC)": BTC, "Amount(USD)": USD}
    x = mycol.insert_one(mydict)
