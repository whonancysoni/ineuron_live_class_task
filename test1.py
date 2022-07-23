import pymongo

client = pymongo.MongoClient("mongodb+srv://nancy2255:Nancy2255@nancy.643d0ns.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db1 = client['mongotest']
coll = db1['test']



#data = coll.find({"companyName": "ineuron"})
data = coll.find({"courseOffered":{"$gt":"E"}})
for i in data:
    print(i)