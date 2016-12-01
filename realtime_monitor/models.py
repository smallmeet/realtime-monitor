from pymysql.connections import Connection

class BaseConn(Connection):
    def __init__(self, config):
        super().__init__(host=config['host'], port=int(config['port']), user=config['user'], passwd=config['passwd'], db=config['db'], charset='utf8')

class Graph(BaseConn):
    def __init__(self, config):
        super().__init__(config)

    def create(self):
        cur = self.cursor()
        cur.execute('CALL create_graph()')
        self.commit()
        cur.close()

    def changeName(self, graphId, name):
        cur = self.cursor()
        cur.execute('CALL change_graph_name({graphId}, \'{name}\')'.format(graphId=graphId, name=name))
        self.commit()
        cur.close()

    def delete(self, graphId):
        cur = self.cursor()
        cur.execute('CALL delete_graph({graphId})'.format(graphId=graphId))
        self.commit()
        cur.close()
