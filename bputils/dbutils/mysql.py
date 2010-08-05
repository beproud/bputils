#:coding=utf-8:

def MySQLConnection(connect_info):
    ''' 単純にMySQLのコネクションを作って返します。 '''
    import MySQLdb
    return MySQLdb.connect(**connect_info)

class MySQLCursor(object):
    """
    MySQLdb用のカーサークラス。

    connection = get_connection({
        'db' : "imagawa",
        'host' : "127.0.0.1",
        'port' : 3306,
        'user' : "user",
        'passwd' : "password"
    })
    cursor = low_level_cursor(connection)
    cursor.query('select id, name, email from huge_data')
    for i in cursor:
        # do something...
    """

    def __init__(self, connection, rows=1, value_type=1):
        self.connection = connection
        self.rows = rows
        self.value_type = value_type
        self.rs = None
        self.row = None
    
    def query(self, sql):
        self.connection.query(sql)
        self.rs = self.connection.use_result()
    
    def has_next(self):
        self.row = self.rs.fetch_row(self.rows, self.value_type)
        return bool(self.row)
    
    def next(self):
        return self.row[0] if self.rows == 1 else self.row
    
    def __iter__(self):
        while(self.has_next()):
            yield self.next()

