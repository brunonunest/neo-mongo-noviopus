from py2neo import Graph
import pymongo
import ssl
from querydata import allrels
from decouple import config

mongourl = config('MONGO_URL')
neo4jurl = config('NEO4J_URL')
neo4jpw = config('NEO4J_PW')

ssl._create_default_https_context = ssl._create_unverified_context
graph = Graph(neo4jurl, password=neo4jpw)
mongolist = []
client = pymongo.MongoClient(mongourl)

for index in range(len(allrels)):
    nodelabel = allrels[index]["node"]
    query = allrels[index]["query"]
    run = graph.run(query).data()
    for obj in run:
        mongolist.append(obj)
    db = client.neo4jrels
    collection = db[nodelabel]
    collection.drop()
    collection = db[nodelabel]
    x = collection.insert_many(mongolist)
    mongolist = []
print("Done uploading")