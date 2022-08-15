#set vars, parameters and imports before start
from py2neo import Graph
from querydata import allnodes
from decouple import config

mongourl = config('MONGO_URL')
neo4jurl = config('NEO4J_URL')
neo4jpw = config('NEO4J_PW')
neo4jurlcareer = config('NEO4J_URL_CAREER')

#OUT will get data from n4oj main DB to INPUT on neo4j career, sync only this way!
graphOutput = Graph(neo4jurl, password=neo4jpw)
graphInput = Graph(neo4jurlcareer, password=neo4jpw)

for k, v in allnodes.items():
    if k == 'User':
        nodelabel = k
        queryOutput = v
        run = graphOutput.run(queryOutput).data()     
        for obj in run:
            email = str(obj['n']['email'])
            firstname = str(obj['n']['firstname'])
            id = str(obj['n']['id'])
            id_ = str(obj['n']['id_'])
            lastname = str(obj['n']['lastname'])
            password = str(obj['n']['password'])
            productionUse = obj['n']['productionUse']
            queryInput = "MERGE (n:User {id_:" + "'" + id_ + "'" + "}) "\
                        "SET n.email = " + "'" + email + "'" + ",n.firstname = " + "'" + firstname + "'" + ",n.id = " + "'" + id + "'" + ",n.lastname = " + "'" + lastname + "'" + ",n.password = " + "'" + password + "'" + ",n.productionUse = " + "'" + productionUse + "'" + " "
            frun = graphInput.run(queryInput).data() 
print("Done uploading User Nodes to Career")


#OUTPUT IS MAIN, INPUT IS CAREER (ALSO ONLY FOR READING)
#NEVER forget the maindatabase is the only way to WRITE!
