from pymysql.connections import Connection

class BaseConn(Connection):
    def __init__(self, config):
        super().__init__(host=config['host'], port=int(config['port']), user=config['user'], passwd=config['passwd'], db=config['db'], charset='utf8')
