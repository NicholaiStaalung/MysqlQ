# MysqlQ 

Handler for mysql queries, intended for data dashboards. (Not data management)

USE THIS SCRIPT WITH CAUTION. IF YOU DO NOT HAVE ANY EXPERIENCE WITH SQL INJECTION THEN DO NOT USE WITH USER INPUT. THE SCRIPT REQUIRES SOME EXPERIENCE WITH MySQL SYNTAX.

## 1st Step

Setup config.py. 

Use your MySQL credentials. Update directly in file

## 2nd Step

Perform QUERY.

Example:

```
query = mysqlQuery().select('something').table('someTable').where('something', 'islogical', 'toSomething').where('someOtherThing', 'isLogical', 'TosomeOtherThing').execute()
```

## 3rd Step

Extract data.

```
data = query.data
```

