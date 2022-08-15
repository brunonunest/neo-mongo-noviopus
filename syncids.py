#pipeline to set ids related to ondata, helping set relation properties

import pandas as pd

#example uses 2 .csv files, regarding relations and nodes from neo4j
dfrels = pd.read_csv('relsjobtitlesubcategory.csv')
dfnodes = pd.read_csv('jobsubcategory.csv')


listrel = dfrels.values.tolist()
listnode = dfnodes.values.tolist()

for obj in listrel:
    for obj2 in listnode:
        print(obj2[0])
        print(obj[3])


for index in range(len(listrel)):
    for index2 in range(len(listnode)):
        if listrel[index][3] == listnode[index2][0]:
            listrel[index][3] = listnode[index2][2]
            print("Match")

#example uses FINALrelsjobtitlesubcategory.csv
dflist = pd.DataFrame(listrel)
dflist.to_csv('FINALrelsjobtitlesubcategory.csv', index=False)