from pymongo import MongoClient


# Connect to your MongoDB cluster.
client = MongoClient()

# List all databases in the cluster.
for db_name in client.list_database_names():
   print(db_name)



