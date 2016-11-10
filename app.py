from flask import Flask, redirect, url_for, render_template
from database import connection, load_config
from load_page_data import device_list, graph_list

app = Flask(__name__)
conn = connection.Connection(load_config.loadConfig('config.json'))

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
    cur.execute('SELECT graph.id, graph.ordering FROM graph WHERE graph.activated=1')
    graphes = []
    for row in cur:
        graphes.append(row)

    result = {}
    for graph in graphes:
        graphId = 'g' + str(graph[0])

        if graphId not in result:
            result[graphId] = {}
            result[graphId]['order'] = graph[1]
            result[graphId]['devices'] = {}

        cur.execute('CALL get_data({graph_id})'.format(graph_id=graph[0])) # device_id, label_id, value, updated
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

@app.route('/static/<path:filename>')
def loadStatic(filename):
    return url_for('static', path=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
