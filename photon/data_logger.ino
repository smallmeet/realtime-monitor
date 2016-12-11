#include "MQTT/MQTT.h"

void callback(char* topic, byte* payload, unsigned int length);

byte server[] = {192, 168, 0, 209};
MQTT client(server, 4000, callback);
String send;
const int LABELS[] = {1, 2, 3, 4, 5};
float values[5];

void callback(char* topic, byte* payload, unsigned int length) {
}

void setup() {
    client.connect(System.deviceID());
}

void loop() {
    for(int j=0; j<10; j++) {
        values[0] = j*0.4;
        values[1] = j*0.3;
        values[2] = j*0.03;
        values[3] = j*0.04;
        values[4] = 1 - values[2] - values[3];

        send = "";
        send += '[';
        for(int i=0; i<5; i++) {
            send += '{';
            send += "\'labelId\':";
            send += LABELS[i];
            send += ",\'value\':";
            send += String(values[i]);
            send += "},";
        }
        send += ']';

        if (client.isConnected()) {
            client.publish("data/insert", send);
            //client.subscribe("###","###");
            delay(200);
        }
    }
}
