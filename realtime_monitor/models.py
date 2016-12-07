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
        self.commit()
        cur.close()

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

    def delete(self, labelId):
        cur = self.cursor()
        cur.execute('CALL delete_label({labelId})'.format(labelId=labelId))
        self.commit()
        cur.close()

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

    def toggleGraph(self, graphId):
        cur = self.cursor()
        cur.execute('CALL toggle_graph({graphId})'.format(graphId=graphId))
        self.commit()
        cur.close()

    def changeOrdering(self, graphId, order):
        cur = self.cursor()
        cur.execute('CALL change_ordering({graphId}, {ordering})'.format(graphId=graphId, ordering=order))
        self.commit()
        cur.close()

    def setInterval(self, graphId, duration, start, finish, dataCount):
        cur = self.cursor()
        cur.execute('CALL set_interval({graphId}, {duration}, {start}, {finish}, {dataCount})'.format(graphId=graphId, duration=duration, start=start, finish=finish, dataCount=dataCount))
        self.commit()
        cur.close()

    def attachLabel(self, graphId, labelId):
        cur = self.cursor()
        cur.execute('CALL attach_label({graphId}, {labelId})'.format(graphId=graphId, labelId=labelId))
        self.commit()
        cur.close()

    def detachLabel(self, graphId, labelId):
        cur = self.cursor()
        cur.execute('CALL detach_label({graphId}, {labelId})'.format(graphId=graphId, labelId=labelId))
        self.commit()
        cur.close()

class Data(BaseConn):
    def __init__(self, config):
        super().__init__(config)

    @staticmethod
    def isFloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    @staticmethod
    def isValid(data):
        if len(data)%2 != 0:
            return False
        for i in range(0, len(data), 2):
            if not Data.isFloat(data[i+1]):
                return False
        return True

    def getCurrentTime(self):
        cur = self.cursor()
        cur.execute('SELECT NOW(6)')
        now = str(cur.fetchone()[0])
        cur.close()
        return now

    def insert(self, labelId, value, updated):
        cur = self.cursor()
        cur.execute('CALL insert_data({labelId}, {value}, \'{updated}\')'.format(labelId=labelId, value=value, updated=updated))
        self.commit()
        cur.close()

    def getData(self, graphId):
        cur = self.cursor()
        result = {}
        cur.execute('CALL get_data({graphId})'.format(graphId=graphId))
        for row in cur:
            labelId = 'l' + str(row[0])

            if labelId not in result:
                result[labelId] = {'value':[], 'updated':[]}
            result[labelId]['value'].append(row[1])
            result[labelId]['updated'].append(str(row[2]))
        cur.close()

        return result
