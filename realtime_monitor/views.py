from flask import render_template, redirect, url_for
from realtime_monitor import app, config
from realtime_monitor.models import BaseConn

@app.route('/')
def index():
    return redirect(url_for('monitor'))

@app.route('/monitor')
def monitor():
    conn = BaseConn(config)
    cur = conn.cursor()

    devices = []
    cur.execute('SELECT device.id, device.name FROM device ORDER BY device.id ASC')
    for row in cur:
        devices.append([int(row[0]), row[1]])

    graphs = []
    cur.execute('SELECT graph.id, graph.name, graph.activated FROM graph ORDER BY graph.activated=1 DESC, graph.ordering ASC, graph.id ASC')
    for row in cur:
        graphs.append([int(row[0]), row[1], row[2]])

    cur.close()
    conn.close()
    return render_template('monitor.html', devices=devices, graphs=graphs)
