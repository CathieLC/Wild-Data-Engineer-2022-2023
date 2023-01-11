from pymongo import MongoClient
import pprint

# connect to MongoDb Cluster with Mongoclient
client = MongoClient()

# Get reference to 'bank' database
db = client.mabdd

# Get a reference to the 'accounts' collection
collection = db.restaurants

# Trouver le nombre de grades A
result = collection.count_documents({'grades.grade': 'A'})
pprint.pprint(f'il y a {result} restaurant avec le grade A')

# Ecris une requête qui trie tous les différents scores de restaurants en ordre décroissant
sort_score = collection.find().sort("grades.score",-1)
for x in sort_score :
    print(x)


restaurant = collection.find({'borough':'/^B/'})
pprint.pprint(restaurant)    




liste = collection.distinct("borough")
restaurant = liste.find


# Ecris une requête qui affiche tous les restaurants si et seulement si le score est inférieur à 20 ou égale à 25, 30, 35 et 40 (n’oubliez pas de préciser que la vérification se fasse sur chaque instance)
score = collection.find({    
    "grades.score" : 
        {'$lt' : 20,
         '$eq': [25,30,35,40]}
         })

for x in score :
    print(x)


# Ecris une requête qui fait la somme du nombre de restaurants par type de cuisine

# Ecris une requête qui ajoute le commentaire “Je gère le NoSQL” pour les boroughs dont le nom commence par “B”

# Ecris une requête qui supprime la clé “adress” des restaurants qui ont un score supérieur à 25

# Ecris une requête qui supprime tous les restaurants dont le nom de quartier est “Queens”


# expliquer ces lignes de codes
varUnwind = {'$unwind' : "$grades"}
varGroup4 = { '$group': {"_id" : "$borough", "moyenne" : {'$avg' : "$grades.score"} } }
varSort2 = {'$sort' : { "moyenne" : -1 } }

result = collection.aggregate( [ varUnwind, varGroup4, varSort2 ] )

for i in result:
    print(i)

'''
*varUnwind* : Sur la valeur grades  
*varGroup4* : groupe par clés id et borough, fait la moyenne des scores  
*varSort2* : Trie dans l'ordre décroissant sur la moyenne

*result* : Calcul

*boucle for* : Affichage des résultats
'''
