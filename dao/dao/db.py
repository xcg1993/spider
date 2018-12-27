from pymysql import Connect
class DB:
    def __init__(self,**kwargs):
        self.host=kwargs.get('host','127.0.0.1')
        self.port = kwargs.get('port', '3306')
        self.username = kwargs.get('user', 'root')
        self.password = kwargs.get('pwd', '123456')
        self.db = kwargs.get('db', 'mysql')
        self.charset = kwargs.get('charset', 'utf8')

