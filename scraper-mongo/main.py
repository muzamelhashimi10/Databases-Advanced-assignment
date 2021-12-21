import pymongo
import redis



r = redis.Redis()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Bitcoin"]
mycol = mydb["Transactions"]


for key in r.keys(pattern="0"):
    Hash = (r.hvals(key)[0]).decode('ascii')
    Time = (r.hvals(key)[1]).decode('ascii')
    BTC = float(r.hvals(key)[2])
    USD = (r.hvals(key)[3]).decode('ascii')
    mydict = {"Hash": Hash, "Time": Time, "Amount(BTC)": BTC, "Amount(USD": USD}
    x = mycol.insert_one(mydict)
