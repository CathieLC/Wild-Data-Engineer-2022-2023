#from dotenv import load_dotenv
from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId

# connect to MongoDb Cluster with Mongoclient
client = MongoClient()

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
account_collection = db.accounts

#filter
document_to_update = {"_id": ObjectId("63bdcdb0b66494415e7f54e4")}

#update (incrément 100$)
add_to_balance = {"$inc" : {"balance" : 100}}

#print original document
pprint.pprint(account_collection.find_one(document_to_update))

#write an expression that adds to the targer account balance by the specified amount
result = account_collection.update_one(document_to_update, add_to_balance)
print("Documents updated : " + str(result.modified_count))

#print updated document
pprint.pprint(account_collection.find_one(document_to_update))

client.close