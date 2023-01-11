
import datetime
from pymongo import MongoClient



# connect to MongoDb Cluster with Mongoclient
client = MongoClient()

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

new_account = {
    "account_holder": "Harry Potter",
    "account_id": "MDB82900133765",
    "account_type": "checking",
    "balance": 434,
    "last_updated": datetime.datetime.utcnow(),
}

# Write an expression that inserts the 'new_account' document into the 'accounts' collection.
result = accounts_collection.insert_one(new_account)

document_id = result.inserted_id
print(f"_id of inserted document: {document_id}")

#client.close()

# Get reference to 'bank' database
db = client.bank

# Get a reference to 'accounts' collection
accounts_collection = db.accounts

new_accounts = [
    {
        "account_id": "MDB0112358132",
        "account_holder": "Burt Lovelace",
        "account_type": "checking",
        "balance": 60250,
    },
    {
        "account_id": "MDB829053201",
        "account_holder": "Sirius Black",
        "account_type": "savings",
        "balance": 896,
    },
]

# Write an expression that inserts the documents in 'new_accounts' into the 'accounts' collection.
result = accounts_collection.insert_many(new_accounts)

document_ids = result.inserted_ids
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")

client.close()



