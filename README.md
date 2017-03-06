
Example use:  
view = mysqlQuery().select('someView').table('someTable').where('something', 'isLogical', 'somethingElse').execute()  
"Beware of user input. This is not a perfect script for portecting against attackers. Carefully filter and check what ypu input into the statements"  
