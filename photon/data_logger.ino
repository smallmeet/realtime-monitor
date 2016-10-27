#include "application.h"
#include "HttpClient/HttpClient.h"

/**
* Declaring the variables.
*/
HttpClient http;

// Headers currently need to be set at init, useful for API keys etc.
http_header_t headers[] = {
    //  { "Content-Type", "application/json" },
    //  { "Accept" , "application/json" },
    { "Accept" , "*/*"},
    { NULL, NULL } // NOTE: Always terminate headers will NULL
};

http_request_t request;
http_response_t response;

const int DEVICE = 1;
const int LABELS[] = {1};
const int LABEL_COUNT = 1;
float values[LABEL_COUNT];

void setup() {
    Serial.begin(9600);
}

void loop() {
    values[0] = analogRead(A0);

    Serial.println();
    Serial.println("Application>\tStart of Loop.");
    // Request path and body can be set at runtime or at setup.
    request.hostname = "192.168.0.43";
    request.port = 3000;
    request.path = "/insert/";
    request.path += DEVICE;
    request.path += '/';
    for(int i=0; i<LABEL_COUNT; i++) {
        request.path += LABELS[i];
        request.path += '/';
        request.path += String(values[i]);
    }

    // The library also supports sending a body with your request:
    //request.body = "{\"key\":\"value\"}";

    // Get request
    http.get(request, response, headers);
    Serial.print("Application>\tResponse status: ");
    Serial.println(response.status);

    Serial.print("Application>\tHTTP Response Body: ");
    Serial.println(response.body);
}
