from flask import Blueprint
from realtime_monitor.models import Graph
import realtime_monitor.json as json

graphPages = Blueprint('graph', __name__)
config = json.loadJSON(open('config.json').readlines())

@graphPages.route('/create')
def createGraph():
    graph = Graph(config)
    newGraph = graph.create()
    graph.close()
    return json.dict2json(newGraph)

@graphPages.route('/change-name/<int:graphId>/<name>')
def changeGraphName(graphId, name):
    graph = Graph(config)
    changedGraph = graph.changeName(graphId, name)
    graph.close()
    return json.dict2json(changedGraph)

@graphPages.route('/delete/<int:graphId>')
def deleteGraph(graphId):
    return 'delete'
