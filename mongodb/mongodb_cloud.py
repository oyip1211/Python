from pymongo import MongoClient
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://admin:FR2017Mongo!@fr-cl0-shard-00-00-uszg6.mongodb.net:27017,fr-cl0-shard-00-01-uszg6.mongodb.net:27017,fr-cl0-shard-00-02-uszg6.mongodb.net:27017/test?ssl=true&replicaSet=FR-CL0-shard-0&authSource=admin")
db=client.profile_repo

serverStatusResult=db.get_collection("repo_core")
pprint(serverStatusResult)