#set vars, parameters and imports before start
from py2neo import Graph
from querydata import onrels
from decouple import config

mongourl = config('MONGO_URL')
neo4jurl = config('NEO4J_URL')
neo4jpw = config('NEO4J_PW')
neo4jurlcareer = config('NEO4J_URL_CAREER')

#OUT will get data from n4oj main DB to INPUT on neo4j career, sync only this way!
graphOutput = Graph(neo4jurl, password=neo4jpw)
graphInput = Graph(neo4jurlcareer, password=neo4jpw)

for index in range(len(onrels)):
    if onrels[index]["label"] == 'Family':
        run = graphOutput.run(onrels[index]["query"]).data()
        for obj in run:
            labelStart = str(obj['labelStart']).replace("[", "").replace("]", "").replace("'", "")
            startNode = str(obj['startNode'])
            endNode = str(obj['endNode'])
            labelEnd = str(obj['labelEnd']).replace("[", "").replace("]", "").replace("'", "")
            id_ = str(obj['id_'])
            close = str(obj['r.close'])
            queryInput = "MATCH (n:" + labelStart + "),(n2:" + labelEnd + ") "\
                        "WHERE n.id_ = " + "'" + startNode + "'" + " and n2.id_ = " + "'" + endNode + "'" + " "\
                        "MERGE (n)-[r:Family]->(n2) "\
                        "SET r.id_ = " + "'" + id_ + "'" + ", r.close = " + "'" + close + "'" + " "
            frun = graphInput.run(queryInput)
print("Done Uploading User Relations to Career")


#OUTPUT IS MAIN, INPUT IS CAREER (ALSO ONLY FOR READING)

#NEVER forget the maindatabase is the only way to WRITE!
