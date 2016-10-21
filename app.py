from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('monitor'))

@app.route('/monitor')
def monitor():
    return 'monitor'

@app.route('/insert/<int:deviceId>/<path:data>')
def insert(deviceId, data):
    # FIXME: check data validation
    return 'insert'

@app.route('/json')
def json():
    return 'json'

if __name__ == '__main__':
    app.run(port=3000, debug=True)
