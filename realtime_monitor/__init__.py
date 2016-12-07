from flask import Flask, url_for, render_template, redirect
from realtime_monitor.models import BaseConn
import realtime_monitor.json as json

from realtime_monitor.controllers import *

app = Flask(__name__)
config = json.loadJSON(open('config.json', 'r').readlines())

app.register_blueprint(devicePages, url_prefix='/device')
app.register_blueprint(labelPages, url_prefix='/label')
app.register_blueprint(graphPages, url_prefix='/graph')
app.register_blueprint(dataPages, url_prefix='/data')

@app.route('/static/<path:filename>')
def loadStatic(filename):
    return url_for('static', path=filename)

import realtime_monitor.views
