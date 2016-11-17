from flask import render_template, redirect, url_for
from realtime_monitor import app, conn
import realtime_monitor.load_page as load_page

@app.route('/')
def index():
    return redirect(url_for('monitor'))

@app.route('/monitor')
def monitor():
    devices = load_page.getDeviceList(conn)
    graphes = load_page.getGraphList(conn)
    return render_template('monitor.html', devices=devices, graphes=graphes)
