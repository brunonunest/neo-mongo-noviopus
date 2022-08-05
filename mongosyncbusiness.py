import pymongo
import ssl
from decouple import config

mongourlout = config('MONGO_URL')
mongourlin = "mongodb://novi_ats_production:bub3XIDmdT8HEjA9@production-shard-00-00-hc0oa.mongodb.net:27017,production-shard-00-01-hc0oa.mongodb.net:27017,production-shard-00-02-hc0oa.mongodb.net:27017/ats_prod?ssl=true&replicaSet=production-shard-0&authSource=admin"
ssl._create_default_https_context = ssl._create_unverified_context
mongolist = []
client = pymongo.MongoClient(mongourlout)
client2 = pymongo.MongoClient(mongourlin)
db = client.neo4jnodes
db2 = client2.ats_prod

#we have data for it but its different
collection = db.jobTitle.find()
collection2 = db2["jobTitle"]
collection2.drop()
collection2 = db2["jobTitle"]
x = collection2.insert_many(collection)
