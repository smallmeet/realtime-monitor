import pymysql

class Connection:
    def __init__(self, config):
        self._host = config['host']
        self._port = int(config['port'])
        self._user = config['user']
        self._passwd = config['passwd']
        self._db = config['db']
        self._charset = 'utf8'
        self._conn = pymysql.connect(host=self._host, port=self._port, user=self._user, passwd=self._passwd, db=self._db, charset=self._charset)

    def getCursor(self):
        return self._conn.cursor()

    def commit(self):
        self._conn.commit()
