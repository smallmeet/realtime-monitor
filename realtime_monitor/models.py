from pymysql.connections import Connection

class BaseConn(Connection):
    def __init__(self, config):
        super().__init__(host=config['host'], port=int(config['port']), user=config['user'], passwd=config['passwd'], db=config['db'], charset='utf8')

class Device(BaseConn):
    def __init__(self, config):
        super().__init__(config)

    def create(self):
        cur = self.cursor()
        cur.execute('CALL create_device()')
        self.commit()
        cur.close()

    def changeName(self, deviceId, name):
        cur = self.cursor()
        cur.execute('CALL change_device_name({deviceId}, \'{name}\')'.format(deviceId=deviceId, name=name))
        self.commit()
        cur.close()

    def delete(self, deviceId):
        cur = self.cursor()
        cur.execute('CALL delete_device({deviceId})'.format(deviceId=deviceId))

class Label(BaseConn):
    def __init__(self, config):
        super().__init__(config)

    def create(self, deviceId):
        cur = self.cursor()
        cur.execute('CALL create_label({deviceId})'.format(deviceId=deviceId))
        self.commit()
        cur.close()

    def changeName(self, labelId, name):
        cur = self.cursor()
        cur.execute('CALL change_label_name({labelId}, \'{name}\')'.format(labelId=labelId, name=name))
        self.commit()
        cur.close()

    def delete(self, deviceId):
        cur = self.cursor()
        cur.execute('CALL delete_label({labelId})'.format(labelId=labelId))

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
