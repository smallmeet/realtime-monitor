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

@app.route('/config/<target>')
def loadConfig(target):
    table = target[0]
    targetId = target[1:]
    conn = BaseConn(config)
    cur = conn.cursor()
    info = []

    if table == 'd':
        cur.execute('SELECT device.name FROM device WHERE device.id={targetId}'.format(targetId=targetId))
        info = list(cur.fetchone())
    elif table == 'g':
        cur.execute('SELECT graph.name, graph.ordering, graph.duration, graph.start, graph.finish, graph.data_count FROM graph WHERE graph.id={targetId}'.format(targetId=targetId))
        info = list(cur.fetchone())
        policy = ''
        if info[2] is not None:
            policy = 'd'
        elif info[3] is not None or info[4] is not None:
            policy = 'sf'
        elif info[5] is not None:
            policy = 'n'
        else:
            policy = 'x'
        cur.execute('SELECT count(graph.activated) FROM graph WHERE graph.activated=1')
        maximum = cur.fetchone()[0] - 1

    cur.close()
    conn.close()
    return render_template('config.html', target=target, info=info, maximum=maximum, policy=policy)

@app.route('/load-list/<target>')
def loadList(target):
    conn = BaseConn(config)
    cur = conn.cursor()
    if target == 'device':
        devices = []
        cur.execute('SELECT device.id, device.name FROM device ORDER BY device.id ASC')
        for row in cur:
            devices.append([int(row[0]), row[1]])
        cur.close()
        conn.close()
        return render_template('load_list.html', target=target, devices=devices)
    elif target == 'graph':
        graphs = []
        cur.execute('SELECT graph.id, graph.name, graph.activated FROM graph ORDER BY graph.activated=1 DESC, graph.ordering ASC, graph.id ASC')
        for row in cur:
            graphs.append([int(row[0]), row[1], row[2]])
        cur.close()
        conn.close()
        return render_template('load_list.html', target=target, graphs=graphs)
