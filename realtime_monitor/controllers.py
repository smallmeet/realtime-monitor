from flask import Blueprint
from realtime_monitor.models import Graph
import realtime_monitor.json as json

graphPages = Blueprint('graph', __name__)
config = json.loadJSON(open('config.json').readlines())

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
