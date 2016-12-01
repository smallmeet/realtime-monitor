from flask import Blueprint
from realtime_monitor.models import *
import realtime_monitor.json as json

devicePages = Blueprint('device', __name__)
graphPages = Blueprint('graph', __name__)
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
