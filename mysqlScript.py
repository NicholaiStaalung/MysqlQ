class mysqlQuery():
    """Simple MySQL queries with escaping, to prevent SQL injection. Intended for data dashboards, not for data management.
    Adjust methods as you please. Returns a numpy array"""

    def __init__(self):
        """Initial function. Opens the connection"""
        global np
        import numpy as np
        global traceback
        import traceback
        import pymysql
        import config as cf

        self.db = pymysql.connect(host = cf.config['host'],    # your host, usually localhost
                             user = cf.config['username'],         # your username
                             passwd = cf.config['password'],  # your password
                             db = cf.config['database']) #Your database
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
        """Use this SELECT method with other methods like table method. Must initiate the string"""
        try:
            if len(self.mysqlString) == 0:
                self.mysqlString += 'SELECT %s' %(select)
            else:
                print 'Error: Bad query call in SELECT method.'
                print 'Check SQL string: %s' %(self.mysqlString)
            return self
        except Exception as err:
            traceback.print_exc()

    def update(self, update):
        """Use this UPDATE method with other methods like table method. Must initiate the string. Currently this method is unavailable due to SQL injection concerns"""
        try:
            if len(self.mysqlString) == 0:
                self.mysqlString += 'UPDATE %s' %(select)
            else:
                print 'Error: Bad query call in UPDATE method.'
                print 'Check SQL string: %s' %(self.mysqlString)
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

    def execute(self, writeColumns=True):
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
                data = np.array(['NO DATA'])
                if num_rows == 0:
                    writeColumns = False
                else:
                    x = map(list, list(results))              # change the type
                    x = sum(x, [])                            # flatten
                    data = np.array(x)
                    data = data.reshape(num_rows, -1)
                if writeColumns:
                    desc = cur.description
                    clm = np.array([item[0].encode('utf-8') for item in desc])[np.newaxis, :]
                    data = np.vstack((clm, data))
                self.data = data
                self.db.close()
                return self
            except Exception as err:
                traceback.print_exc()
