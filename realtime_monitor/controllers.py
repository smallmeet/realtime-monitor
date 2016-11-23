from flask import Blueprint
from realtime_monitor.models import Graph
import realtime_monitor.json as json

graphPages = Blueprint('graph', __name__)

@graphPages.route('/create')
def createGraph():
    graph = Graph(json.loadJSON(open('config.json').readlines()))
    newGraph = graph.create()
    graph.close()
    return json.dict2json(newGraph)

@graphPages.route('/change-name/<int:graphId>/<name>')
def changeGraphName(graphId, name):
    return name

@graphPages.route('/delete/<int:graphId>')
def deleteGraph(graphId):
    return 'delete'
