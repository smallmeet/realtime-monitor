from flask import Flask, redirect, url_for
from database import connection, load_config

app = Flask(__name__)
conn = connection.Connection(load_config.loadConfig('config.json'))

@app.route('/')
def index():
    return redirect(url_for('monitor'))

@app.route('/monitor')
def monitor():
    return 'monitor'

@app.route('/insert/<int:deviceId>/<path:data>')
def insert(deviceId, data):
    # FIXME: check data validation
    # TODO: ues deviceId
    data = data.split('/')
    if len(data)%2 != 0:
        return '404'
    else:
        cur = conn.getCursor()
        cur.execute('SELECT NOW(6)')
        now = cur.fetchone()[0]
        for i in range(0, len(data), 2):
            cur.execute('CALL insert_data({label_id}, {value}, \'{updated}\')'.format(label_id=data[i], value=data[i+1], updated=now))
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
                result[graphId]['devices'][deviceId][labelId] = []
            result[graphId]['devices'][deviceId][labelId].append({'value':row[2], 'updated':str(row[3])})

    cur.close()
    return str(result).replace('\'', '\"')

@app.route('/static/<path:filename>')
def loadStatic(filename):
    return url_for('static', path=filename)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
