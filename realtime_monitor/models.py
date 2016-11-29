from pymysql.connections import Connection

class BaseConn(Connection):
    def __init__(self, config):
        super().__init__(host=config['host'], port=int(config['port']), user=config['user'], passwd=config['passwd'], db=config['db'], charset='utf8')
        self.autocommit_mode = True

class Graph(BaseConn):
    def __init__(self, config):
        super().__init__(config)

    def create(self):
        cur = self.cursor()
        cur.execute('CALL create_graph()')
        cur.execute('SELECT graph.id, graph.name FROM graph WHERE graph.id=LAST_INSERT_ID()')
        row = cur.fetchone()
        self.commit()
        cur.close()
        return {'id':row[0], 'name':row[1]}

    def changeName(self, graphId, name):
        cur = self.cursor()
        cur.execute('CALL change_graph_name({graphId}, \'{name}\')'.format(graphId=graphId, name=name))
        cur.execute('SELECT graph.id, graph.name FROM graph WHERE graph.id={graphId}'.format(graphId=graphId))
        row = cur.fetchone()
        self.commit()
        cur.close()
        return {'id':row[0], 'name':row[1]}
