import pymongo
import ssl
from decouple import config

mongourlout = config('MONGO_URL')
mongourlin = "mongodb+srv://novi_adm1n:UwgvuAW07CzzOD4W@production.orohg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
ssl._create_default_https_context = ssl._create_unverified_context
mongolist = []
client = pymongo.MongoClient(mongourlout)
client2 = pymongo.MongoClient(mongourlin)
db = client.neo4jnodes
db2 = client2.myFirstDatabase

collection = db.jobTitle.find()
collection2 = db2["jobTitle"]
collection2.drop()
collection2 = db2["jobTitle"]
x = collection2.insert_many(collection)

collection = db.skillName.find()
collection2 = db2["skillName"]
collection2.drop()
collection2 = db2["skillName"]
x = collection2.insert_many(collection)

collection = db.jobSubCategory.find()
collection2 = db2["jobSubCategory"]
collection2.drop()
collection2 = db2["jobSubCategory"]
x = collection2.insert_many(collection)

collection = db.jobCategory.find()
collection2 = db2["jobCategory"]
collection2.drop()
collection2 = db2["jobCategory"]
x = collection2.insert_many(collection)

collection = db.fieldOfStudy.find()
collection2 = db2["fieldOfStudy"]
collection2.drop()
collection2 = db2["fieldOfStudy"]
x = collection2.insert_many(collection)

collection = db.degreeName.find()
collection2 = db2["degreeName"]
collection2.drop()
collection2 = db2["degreeName"]
x = collection2.insert_many(collection)

collection = db.instituteType.find()
collection2 = db2["instituteType"]
collection2.drop()
collection2 = db2["instituteType"]
x = collection2.insert_many(collection)

collection = db.interestCategory.find()
collection2 = db2["interestCategory"]
collection2.drop()
collection2 = db2["interestCategory"]
x = collection2.insert_many(collection)

collection = db.interestSubCategory.find()
collection2 = db2["interestSubCategory"]
collection2.drop()
collection2 = db2["interestSubCategory"]
x = collection2.insert_many(collection)

collection = db.interestName.find()
collection2 = db2["interestName"]
collection2.drop()
collection2 = db2["interestName"]
x = collection2.insert_many(collection)
