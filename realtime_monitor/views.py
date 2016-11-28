from flask import render_template, redirect, url_for
from realtime_monitor import app, config
from realtime_monitor.models import BaseConn
import realtime_monitor.load_page as load_page

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
