import pymongo
import ssl
from decouple import config

#STANDBY
#mongourlout = 'mongodb://dedicated_user:4UMwCjPNLGgDPnYkemPHEEEg@development-shard-00-00-hc0oa.mongodb.net:27017,development-shard-00-01-hc0oa.mongodb.net:27017,development-shard-00-02-hc0oa.mongodb.net:27017/novi_dedicated?ssl=true&replicaSet=development-shard-0&authSource=admin'
#mongourlin = "mongodb://novi_ats_production:bub3XIDmdT8HEjA9@production-shard-00-00-hc0oa.mongodb.net:27017,production-shard-00-01-hc0oa.mongodb.net:27017,production-shard-00-02-hc0oa.mongodb.net:27017/ats_prod?ssl=true&replicaSet=production-shard-0&authSource=admin"
ssl._create_default_https_context = ssl._create_unverified_context
mongolist = []
client = pymongo.MongoClient(mongourlout)
client2 = pymongo.MongoClient(mongourlin)
db = client.novi_dedicated
db2 = client2.ats_prod

#we have data for it but its different, check with Karina
#collection = db.jobTitle.find()
#collection2 = db2["jobTitle"]
#collection2.drop()
#collection2 = db2["jobTitle"]
#x = collection2.insert_many(collection)
