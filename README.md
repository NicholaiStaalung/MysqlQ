USE THIS SCRIPT WITH CAUTION. IF YOU DO NOT HAVE ANY EXPERIENCE WITH SQL INJECTION THEN DO NOT USE WITH USER INPUT

1st Step: Setup Config.py. Use your MySQL credentials. Update directly in file

2nd Step: Perform QUERY.
Example:
data = mysqlQuery().select('something').table('someTable').where('something', 'islogical', 'toSomething').where('someOtherThing', 'isLogical', 'TosomeOtherThing').execute()

3rd Step: Extract data.

data = data.data

THE INTENTTION FOR THIS SCRIPT IS TO PROVIDE EASY QUERY STATEMENTS FOR PYTHON DASHBAORDS AND MACHINE LEARNING
