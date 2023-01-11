#from dotenv import load_dotenv
from pymongo import MongoClient
import pprint


# connect to MongoDb Cluster with Mongoclient
client = MongoClient()

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

#filter
select_accounts = {"account_type" : "savings"}

#update (set permet d'ajouter le champ si celui-ci n'existe pas. Nous voulons que la val min soit 100)
set_field = {"$set" : {"minimum_balance" : 100}}


#write an expression that adds a 'minimum balance' field to each savings account and sets its value to 100
#on passe d'abord le filtre (select account) puis la mise à jour (set field)
result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched : " + str(result.matched_count))
print("Documents updated : " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts))


client.close