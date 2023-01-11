#from dotenv import load_dotenv
from pymongo import MongoClient
import pprint



# connect to MongoDb Cluster with Mongoclient
client = MongoClient()

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Filter by ObjectId
document_to_delete = {"balance": {"$lt": 2000}}

# Search for sample document before delete
print("Searching for sample target document before delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

# Write an expression that deletes the target accounts.
result = accounts_collection.delete_many(document_to_delete)

# Search for sample document after delete
print("Searching for sample target document after delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

print("Document deleted : " + str(result.deleted_count))


client.close()