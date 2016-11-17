from flask import Flask, redirect, url_for, render_template
from realtime_monitor.database import connection
import realtime_monitor.json as json
from realtime_monitor.load_page_data import device_list, graph_list
from realtime_monitor.validation import valid_path

app = Flask(__name__)
conn = connection.Connection(json.loadJSON(open('config.json', 'r').readlines()))

@app.route('/')
def index():
    return redirect(url_for('monitor'))

@app.route('/monitor')
def monitor():
    devices = device_list.getDeviceList(conn)
    graphes = graph_list.getGraphList(conn)
    return render_template('monitor.html', devices=devices, graphes=graphes)

@app.route('/insert/<int:deviceId>/<path:data>')
def insert(deviceId, data):
    # TODO: ues deviceId
    if valid_path.isValid(data):
        return '404'

    pair = []
    for i in range(0, len(data), 2):
        pair.append([data[i], data[i+1]])
    cur = conn.getCursor()
    cur.execute('SELECT NOW(6)')
    now = cur.fetchone()[0]
    for i in range(0, len(pair)):
        cur.execute('CALL insert_data({labelId}, {value}, \'{updated}\')'.format(labelId=pair[i][0], value=pair[1][i+1], updated=now))
    conn.commit()
    cur.close()
    return '200'

@app.route('/json')
def getData():
    cur = conn.getCursor()
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
    return json.dict2json(result)

@app.route('/static/<path:filename>')
def loadStatic(filename):
    return url_for('static', path=filename)
