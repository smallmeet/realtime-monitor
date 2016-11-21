from flask import Flask, url_for, render_template, redirect
from realtime_monitor.models import BaseConn
import realtime_monitor.json as json
import realtime_monitor.load_page as load_page
from realtime_monitor.validation import valid_path

from realtime_monitor.controllers import *

app = Flask(__name__)
config = json.loadJSON(open('config.json', 'r').readlines())

app.register_blueprint(graphPages, url_prefix='/graph')

@app.route('/')
def index():
    return redirect(url_for('monitor'))

@app.route('/monitor')
def monitor():
    conn = BaseConn(config)
    devices = load_page.getDeviceList(conn)
    graphes = load_page.getGraphList(conn)
    conn.close()
    return render_template('monitor.html', devices=devices, graphes=graphes)

@app.route('/insert/<int:deviceId>/<path:data>')
def insert(deviceId, data):
    # TODO: ues deviceId
    data = data.split('/')
    if not valid_path.isValid(data):
        return '404'

    conn = BaseConn(config)
    pair = []
    for i in range(len(data)//2):
        pair.append([data[2*i], data[2*i+1]])
    cur = conn.cursor()
    cur.execute('SELECT NOW(6)')
    now = cur.fetchone()[0]
    for i in range(0, len(pair)):
        cur.execute('CALL insert_data({labelId}, {value}, \'{updated}\')'.format(labelId=pair[i][0], value=pair[i][1], updated=now))
    conn.commit()
    cur.close()
    conn.close()
    return '200'

@app.route('/json')
def getData():
    conn = BaseConn(config)
    cur = conn.cursor()
    cur.execute('SELECT graph.id FROM graph WHERE graph.activated=1')
    graphes = []
    for row in cur:
        graphes.append(row)

    result = {}
    for graph in graphes:
        graphId = str(graph[0])

        if graphId not in result:
            result[graphId] = {}

        cur.execute('CALL get_data({graphId})'.format(graphId=graphId)) # label_id, value, updated
        for row in cur:
            labelId = 'l' + str(row[0])

            if labelId not in result[graphId]:
                result[graphId][labelId] = {'value':[], 'updated':[]}
            result[graphId][labelId]['value'].append(row[1])
            result[graphId][labelId]['updated'].append(str(row[2]))

    cur.close()
    conn.close()
    return json.dict2json(result)

@app.route('/static/<path:filename>')
def loadStatic(filename):
    return url_for('static', path=filename)
