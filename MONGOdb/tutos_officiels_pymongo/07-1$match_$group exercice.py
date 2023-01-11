#from dotenv import load_dotenv
from pymongo import MongoClient
import pprint

# connect to MongoDb Cluster with Mongoclient
client = MongoClient()

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts


# Calculate the average balance of checking and savings accounts with balances of less than $1000.

# Select accounts with balances of less than $1000.
select_by_balance = {"$match" : {"balance" : {"lt" : 1000}}}

# Separate documents by account type and calculate the average balance for each account type.
separate_by_account_calculate_avg_balance = {"$group" : {"_id" : "$account_type", "avgbalance" : {"$avg" : "$balance"}}}


#create an aggregation pipeline using 'stage_match_balance' and 'stage_group_account_type'
pipeline = [select_by_balance,separate_by_account_calculate_avg_balance]

# Perform an aggregation on 'pipeline'.
results = accounts_collection.aggregate(pipeline)

print()
print(
    "Average balance of checking and savings accounts with balances of less than $1000:", "\n"
)

for item in results:
    pprint.pprint(item)

client.close()
