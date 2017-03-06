class mysqlQuery():
    """MySQL queries with escaping, to prevent SQL injection. Returns a numpy array"""

    def __init__(self):
        """Initial function. Opens the connection"""
        global np
        import numpy as np
        global traceback
        import traceback
        import pymysql
        self.db = pymysql.connect(host = '',    # your host, usually localhost
                             user = '',         # your username
                             passwd = '',  # your password
                             db = '')
        self.mysqlString = ''


    def getFullTable(self, tableName):
        """Create a Table Query"""
        try:
            self.tableName = tableName
            cur = self.db.cursor()
            self.mysqlString += "SELECT * FROM %s" %(self.tableName)
            return self
        except Exception as err:
            traceback.print_exc()

    def getFullView(self, viewName, tableName, whereStatement=False):
        """Create a View Query.
        Seperate Where statement string with logical operators and remember proper quotes.
        Requires som experience with MySQL syntax"""
        try:
            self.mysqlString += "SELECT %s FROM %s" %(viewName, tableName)
            if whereStatement != False:
                self.mysqlString = self.mysqlString + ' WHERE %s' %(whereStatement)
        except Exception as err:
            traceback.print_exc()

        return self

    def select(self, select):
        """Use this method with other methods like table method"""
        try:
            self.mysqlString += 'SELECT %s' %(select)
            return self
        except Exception as err:
            traceback.print_exc()

    def table(self, table):
        """Use table method with the view method and where statements"""
        try:
            self.mysqlString += ' FROM %s' %(table)
            return self
        except Exception as err:
            traceback.print_exc()


    def where(self, column, logic, datapoint):
        """Adding a where statement to the SQL statement"""
        try:
            if not 'WHERE' in self.mysqlString:
                self.mysqlString += " WHERE %s%s'%s'" %(column, logic, datapoint)
            elif 'WHERE' in self.mysqlString:
                self.mysqlString += " AND %s%s'%s'" %(column, logic, datapoint)
            return self
        except Exception as err:
            traceback.print_exc()

    def execute(self):
        """Executing the SQL statement"""
        if ';' in self.mysqlString or '-' in self.mysqlString:
            print 'Error: Possible SQL injection. Escaping the procedure'
            print 'Check statement: %s' %(self.mysqlString)
        else:
            try:
                cur = self.db.cursor()
                cur.execute(self.mysqlString)
                results = cur.fetchall()
                num_rows = int(cur.rowcount)
                x = map(list, list(results))              # change the type
                x = sum(x, [])                            # flatten
                data = np.array(x)
                self.data = data.reshape(num_rows, -1)
                self.db.close()
                return self
            except Exception as err:
                traceback.print_exc()
