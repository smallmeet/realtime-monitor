from flask import Blueprint
from realtime_monitor.models import *
import realtime_monitor.json as json

devicePages = Blueprint('device', __name__)
graphPages = Blueprint('graph', __name__)
dataPages = Blueprint('data', __name__)
config = json.loadJSON(open('config.json').readlines())

@devicePages.route('/create')
def createDevice():
    device = Device(config)
    device.create()
    device.close()
    return 'create'

@devicePages.route('/change-name/<int:deviceId>/<name>')
def changeDeviceName(deviceId, name):
    device = Device(config)
    device.changeName(deviceId, name)
    device.close()
    return 'change'

@devicePages.route('/delete/<int:deviceId>')
def deleteDevice(deviceId):
    device = Device(config)
    device.delete(deviceId)
    device.close()
    return 'delete'

@graphPages.route('/create')
def createGraph():
    graph = Graph(config)
    graph.create()
    graph.close()
    return 'create'

@graphPages.route('/change-name/<int:graphId>/<name>')
def changeGraphName(graphId, name):
    graph = Graph(config)
    graph.changeName(graphId, name)
    graph.close()
    return 'change'

@graphPages.route('/delete/<int:graphId>')
def deleteGraph(graphId):
    graph = Graph(config)
    graph.delete(graphId)
    graph.close()
    return 'delete'

@dataPages.route('/insert/<int:deviceId>/<path:dataList>')
def insert(deviceId, dataList):
    dataList = dataList.split('/')
    if not Data.isValid(dataList):
        return '404'
    data = Data(config)
    pair = []
    for i in range(len(dataList)//2):
        pair.append([dataList[2*i], dataList[2*i+1]])
    now = data.getCurrentTime()
    for i in range(len(pair)):
        data.insert(pair[i][0], pair[i][1], now)
    data.close()
    return 'insert'

@dataPages.route('/get')
def getData():
    data = Data(config)
    cur = data.cursor()
    cur.execute('SELECT graph.id FROM graph WHERE graph.activated=1')
    graphs = []
    for row in cur:
        graphs.append(row)

    result = {}
    for graph in graphs:
        graphId = str(graph[0])
        result[graphId] = data.getData(graphId)

    cur.close()
    data.close()
    return json.dict2json(result)
