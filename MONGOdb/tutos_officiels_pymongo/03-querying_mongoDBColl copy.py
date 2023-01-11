from pymongo import MongoClient
import pprint

# Import ObjectId from bson package (part of Pymongo distribution) to enable querying by ObjectId
from bson.objectid import ObjectId

# connect to MongoDb Cluster with Mongoclient
client = MongoClient()

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Query by ObjectId
document_to_find = {"_id": ObjectId("63bd39c7baae8d2b1cf57cb1")}

# Write an expression that retrieves the document matching the query constraint in the 'accounts' collection.
result = accounts_collection.find_one(document_to_find)
pprint.pprint(result)

