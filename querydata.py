allnodes = {"interestCategory": "MATCH (n:interestCategory) SET n.`id_` = ID(n) RETURN n", "interestSubCategory": "MATCH (n:interestSubCategory) SET n.`id_` = ID(n) RETURN n", "interestName": "MATCH (n:interestName) SET n.`id_` = ID(n) RETURN n", "translation": "MATCH (n:translation) SET n.`id_` = ID(n) RETURN n", "skillName": "MATCH (n:skillName) SET n.`id_` = ID(n) RETURN n", "skill": "MATCH (n:skill) SET n.`id_` = ID(n) RETURN n", "jobTitle": "MATCH (n:jobTitle) SET n.`id_` = ID(n) RETURN n", "jobName": "MATCH (n:jobName) SET n.`id_` = ID(n) RETURN n", "jobSubCategory": "MATCH (n:jobSubCategory) SET n.`id_` = ID(n) RETURN n", "jobCategory": "MATCH (n:jobCategory) SET n.`id_` = ID(n) RETURN n", "interest": "MATCH (n:interest) SET n.`id_` = ID(n) RETURN n", "instituteType": "MATCH (n:instituteType) SET n.`id_` = ID(n) RETURN n", "fieldName": "MATCH (n:fieldName) SET n.`id_` = ID(n) RETURN n", "fieldOfStudy": "MATCH (n:fieldOfStudy) SET n.`id_` = ID(n) RETURN n", "degreeType": "MATCH (n:degreeType) SET n.`id_` = ID(n) RETURN n", "Database": "MATCH (n:Database) SET n.`id_` = ID(n) RETURN n", "Message": "MATCH (n:Message) SET n.`id_` = ID(n) RETURN n", "User": "MATCH (n:User) SET n.`id_` = ID(n) RETURN n", "degreeName": "MATCH (n:degreeName) SET n.`id_` = ID(n) RETURN n"}
allrels = [{"node": "Family", "query": "MATCH (a)-[r:Family]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "SAYS", "query": "MATCH (a)-[r:SAYS]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "degreeDegreeName","query": "MATCH (a)-[r:degreeDegreeName]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "degreeTypeInstituteType", "query": "MATCH (a)-[r:degreeTypeInstituteType]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "fieldFieldName","query": "MATCH (a)-[r:fieldFieldName]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "fieldOfStudyFieldOfStudy","query": "MATCH (a)-[r:fieldOfStudyFieldOfStudy]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "fieldOfStudyInstituteType","query": "MATCH (a)-[r:fieldOfStudyInstituteType]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "interestCategorySubcategory","query": "MATCH (a)-[r:interestCategorySubcategory]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "interestInterestName","query": "MATCH (a)-[r:interestInterestName]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "interestInterestSubcategory","query": "MATCH (a)-[r:interestInterestSubcategory]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "jobCategorySubcategory","query": "MATCH (a)-[r:jobCategorySubcategory]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "jobTitleJobName","query": "MATCH (a)-[r:jobTitleJobName]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "jobTitleJobTitle","query": "MATCH (a)-[r:jobTitleJobTitle]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "jobTitleSubcategory","query": "MATCH (a)-[r:jobTitleSubcategory]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "skillSkill", "query": "MATCH (a)-[r:skillSkill]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "skillSkillName","query": "MATCH (a)-[r:skillSkillName]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}, {"node": "skillSubcategory","query": "MATCH (a)-[r:skillSubcategory]->(b) RETURN labels(a) as labelStart, ID(a) as startNode, ID(b) as endNode, labels(b) as labelEnd, ID(r) as id_"}]