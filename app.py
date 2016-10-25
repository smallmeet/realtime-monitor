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
    return 'json'

@app.route('/static/<path:filename>')
def loadStatic(filename):
    return url_for('static', path=filename)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
