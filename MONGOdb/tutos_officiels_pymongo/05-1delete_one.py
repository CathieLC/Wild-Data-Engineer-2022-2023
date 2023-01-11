#from dotenv import load_dotenv
from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId


# connect to MongoDb Cluster with Mongoclient
client = MongoClient()

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Filter by ObjectId
document_to_delete = {"_id": ObjectId("63bdcdb0b66494415e7f54e4")}

# Search for document before delete
print("Searching for target document before delete : ")
pprint.pprint(accounts_collection.find_one(document_to_delete))


# Write an expression that deletes the target account.
result = accounts_collection.delete_one(document_to_delete)

# Search for document after delete
print("Searching for target document after delete : ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

print("Document deleted : " + str(result.deleted_count))


client.close()