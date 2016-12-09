import paho.mqtt.client as mqtt

from realtime_monitor import config
from realtime_monitor.models import Data
from datetime import datetime

def on_connect(client, userdata, rc):
    print("Connected")
    client.subscribe("data/insert")

def on_message(client, userdata, msg):
    data = Data(config)
    msgList = eval(msg.payload)
    now = datetime.now().isoformat().replace('T', ' ').strip()
    for d in msgList:
        data.insert(d['labelId'], d['value'], now)
        print(d['labelId'], d['value'], now)
    data.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('localhost', 4000, 60)

client.loop_forever()
