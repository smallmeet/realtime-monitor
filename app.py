from flask import Flask, redirect, url_for, render_template
from database import connection, load_config

app = Flask(__name__)
conn = connection.Connection(load_config.loadConfig('config.json'))

@app.route('/')
def index():
    return redirect(url_for('monitor'))

@app.route('/monitor')
def monitor():
    return render_template('monitor.html')

@app.route('/insert/<int:deviceId>/<path:data>')
def insert(deviceId, data):
    # TODO: ues deviceId
    def isFloat(number):
        try:
            float(number)
            return True
        except ValueError:
            return False

    data = data.split('/')
    if len(data)%2 != 0:
        return '404'
    else:
        pair = []
        for i in range(0, len(data), 2):
            if not data[i].isdigit() or not isFloat(data[i+1]):
                print('Invalid data pair')
                continue
            else:
                pair.append([data[i], data[i+1]])
        cur = conn.getCursor()
        cur.execute('SELECT NOW(6)')
        now = cur.fetchone()[0]
        for i in range(0, len(pair)):
            cur.execute('CALL insert_data({label_id}, {value}, \'{updated}\')'.format(label_id=pair[i][0], value=pair[1][i+1], updated=now))
        conn.commit()
        cur.close()
        return '200'

@app.route('/json')
def json():
    cur = conn.getCursor()
    cur.execute('SELECT `id`, `duration`, `from`, `to`, `order` FROM graph WHERE `activated`=1')
    graphes = []
    for row in cur:
        graphes.append(row)

    result = {}
    for graph in graphes:
        graphId = 'g' + str(graph[0])

        if graphId not in result:
            result[graphId] = {}
            result[graphId]['order'] = graph[4]
            result[graphId]['devices'] = {}

        if graph[1] is None:
            if graph[3] is None: # from
                query = 'CALL get_data_from({graph_id}, {f})'.format(graph_id=graph[0], f=graph[2])
            else: # to
                query = 'CALL get_data_from_to({graph_id}, {f}, {t})'.format(graph_id=graph[0], f=graph[2], t=graph[3])
        else: # realtime
            query = 'CALL get_data_in_realtime({graph_id}, {duration})'.format(graph_id=graph[0], duration=graph[1])

        cur.execute(query) # device_id, label_id, value, updated
        for row in cur:
            deviceId = 'd' + str(row[0])
            labelId = 'l' + str(row[1])

            if deviceId not in result[graphId]['devices']:
                result[graphId]['devices'][deviceId] = {}
            if labelId not in result[graphId]['devices'][deviceId]:
                result[graphId]['devices'][deviceId][labelId] = {'value':[], 'updated':[]}
            result[graphId]['devices'][deviceId][labelId]['value'].append(row[2])
            result[graphId]['devices'][deviceId][labelId]['updated'].append(str(row[3]))

    cur.close()
    return str(result).replace('\'', '\"')

@app.route('/plots')
def loadDashboard():
    cur = conn.getCursor()
    cur.execute('SELECT graph.id, graph.order FROM graph WHERE graph.activated=1')
    plots = []
    for row in cur:
        plots.insert(int(row[1]), int(row[0]))
    cur.close()
    return render_template('plots.html', plots=plots)

@app.route('/graphes')
def loadGraphes():
    cur = conn.getCursor()
    labels = conn.getCursor()
    activated = []
    inactivated = []
    cur.execute('SELECT graph.id, graph.name, graph.activated FROM graph ORDER BY graph.activated DESC, graph.order ASC')
    for row in cur:
        if int(row[2]) == 1: # activated
            graphes = activated
        else:
            graphes = inactivated
        graphes.append([int(row[0]), row[1]])
        labels.execute('SELECT label.id, label.name FROM label, connects WHERE connects.graph_id={gid} AND label.id=connects.label_id'.format(gid=int(row[0])))
        graphes[-1].append([[int(l[0]), l[1]] for l in labels])
    labels.close()
    cur.close()
    return render_template('graphes.html', activated=activated, inactivated=inactivated)

@app.route('/devices')
def loadDevices():
    cur = conn.getCursor()
    labels = conn.getCursor()
    devices = []
    cur.execute('SELECT device.id, device.name FROM device')
    for row in cur:
        devices.append([int(row[0]), row[1]])
        labels.execute('SELECT label.id, label.name FROM label, includes WHERE includes.device_id={did} AND label.id=includes.label_id'.format(did=int(row[0])))
        devices[-1].append([[int(l[0]), l[1]] for l in labels])
    labels.close()
    cur.close()
    return render_template('devices.html', devices=devices)

@app.route('/static/<path:filename>')
def loadStatic(filename):
    return url_for('static', path=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
