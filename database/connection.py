import pymysql

class Connection:
    def __init__(self, config):
        self._conn = pymysql.connect(host=config['host'], port=int(config['port']), user=config['user'], passwd=config['passwd'], db=config['db'], charset='utf8')

    def getCursor(self):
        return self._conn.cursor()
