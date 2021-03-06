from flask import Blueprint, request
from realtime_monitor.models import *
import realtime_monitor.json as json

devicePages = Blueprint('device', __name__)
labelPages = Blueprint('label', __name__)
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

@labelPages.route('/create/<int:deviceId>')
def createLabel(deviceId):
    label = Label(config)
    label.create(deviceId)
    label.close()
    return 'create'

@labelPages.route('/change-name/<int:labelId>/<name>')
def changeLabelName(labelId, name):
    label = Label(config)
    label.changeName(labelId, name)
    label.close()
    return 'change'

@labelPages.route('/delete/<int:labelId>')
def deleteLabel(labelId):
    label = Label(config)
    label.delete(labelId)
    label.close()
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

@graphPages.route('/toggle/<int:graphId>')
def toggleGraph(graphId):
    graph = Graph(config)
    graph.toggleGraph(graphId)
    graph.close()
    return 'toggle'

@graphPages.route('/order/<int:graphId>/<int:order>')
def changeOrdering(graphId, order):
    graph = Graph(config)
    graph.changeOrdering(graphId, order)
    graph.close()
    return 'order'

@graphPages.route('/set-interval/<int:graphId>', methods=['POST'])
def setInterval(graphId):
    graph = Graph(config)
    start = request.form['start']
    finish = request.form['finish']

    if len(start)==0:
        start = 'NULL'
    if len(finish)==0:
        finish = 'NULL'

    if start != 'NULL':
        start = '\'' + start + '\''
    if finish != 'NULL':
        finish = '\'' + finish + '\''

    graph.setInterval(graphId, request.form['duration'], start, finish, request.form['data-count'])
    graph.close()
    return 'interval'

@graphPages.route('/attach/<int:graphId>/<int:labelId>')
def attachLabel(graphId, labelId):
    graph = Graph(config)
    graph.attachLabel(graphId, labelId)
    graph.close()
    return 'attach'

@graphPages.route('/detach/<int:graphId>/<int:labelId>')
def detachLabel(graphId, labelId):
    graph = Graph(config)
    graph.detachLabel(graphId, labelId)
    graph.close()
    return 'attach'

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
