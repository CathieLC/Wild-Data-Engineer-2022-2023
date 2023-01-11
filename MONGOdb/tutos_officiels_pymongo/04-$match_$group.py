#from dotenv import load_dotenv
from pymongo import MongoClient
import pprint

# connect to MongoDb Cluster with Mongoclient
client = MongoClient()

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

'''
Utilisation des étapes d'agrégation MongoDB avec Python : $match et $group
Passez en revue le code suivant, qui montre comment utiliser les étapes et dans un pipeline d'agrégation MongoDB à l'aide de PyMongo.$match$group
Utiliser $match
Lorsque nous créons des requêtes à l'aide du cadre d'agrégation, chaque étape transforme ou organise les données d'une manière spécifique. Dans cette leçon, nous avons utilisé les étapes et .$match$group
Utilisez l' opérateur pour sélectionner les documents qui correspondent aux conditions de requête spécifiées et transmettre les documents correspondants à l'étape suivante. prend un document qui spécifie la requête.$match$match
$matchdoivent être placés tôt dans un pipeline pour réduire le nombre de documents qui seront traités plus tard dans le pipeline.
'''
# Select accounts with balances of less than $1000.
select_by_balance = {"$match": {"balance": {"$lt": 1000}}}

'''
Utilisation de $groupe
Utilisez la scène pour séparer les documents en groupes. 
L' étape doit avoir un champ qui spécifie la clé de groupe. La clé de groupe est précédée d'un et entourée de guillemets.$group$group_id$
Une étape peut inclure des champs supplémentaires qui sont calculés à l'aide d'opérateurs d'accumulateur, tels que .$group$avg
Voici un exemple de scène :$group
'''

# Separate documents by account type and calculate the average balance for each account type.
separate_by_account_calculate_avg_balance = {
    "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
}

'''
Exemple d'agrégation utilisant $match et $group
Voici un exemple de pipeline d'agrégation qui utilise et .$match$group
'''

# Create an aggegation pipeline using 'stage_match_balance' and 'stage_group_account_type'.
pipeline = [
    select_by_balance,
    separate_by_account_calculate_avg_balance,
]

# Perform an aggregation on 'pipeline'.
results = accounts_collection.aggregate(pipeline)

print()
print(
    "Average balance of checking and savings accounts with balances of less than $1000:", "\n"
)

for item in results:
    pprint.pprint(item)

