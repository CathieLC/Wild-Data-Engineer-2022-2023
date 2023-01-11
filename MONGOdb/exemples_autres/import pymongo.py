import pymongo

connection = pymongo.MongoClient()
db = connection.mabdd
col = db.Restaurants

# This is a cursor instance
cur = col.find()

results = list(cur)

# Checking the cursor is empty
# or not
if len(results)==0:
	print("Empty Cursor")
else:
	print("Cursor is Not Empty")
	print("Do Stuff Here")
