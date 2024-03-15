#include <stdint.h>
#include <WiFi.h>
#include <ArduinoJson.h>

const char* ssid = "ESP32AP";
const char* password = "password";

WiFiClient client;
WiFiServer server(80);


uint16_t data[30000]; // analog one 
//uint16_t data2[20000]; // analog two 
const int SAMPLE_INTERVAL = 100;  // 500 microseconds
int runCheck = 0;
int x = 0;
int sending = 0;
int val =0; //value read in from the pin
int val2 = 0;
int running = 0; 



void setup(){
  //baud rate
  Serial.begin(250000);

  //init the wifi server using the defined SSID and password
  WiFi.softAP(ssid, password);
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
  server.begin();

  //set the mode of the pins
  pinMode(25, INPUT);
  //pinMode(20, INPUT); //**Change this one for the new microphone**
  pinMode(32, INPUT);


  //wait until a device is connected 
  client = server.available();
  while (! client.connected()) {
    client = server.available();
    delay(2000);
    Serial.println("Waiting for device to connect");
  }

  //device connected => proceed
  Serial.println("Device successfully connected");
  client.println("Connected Successfully");

  
}


void loop() {
  //check for an input string
  if((running == 0) && (sending == 0))
  {
    runCheck = Serial.parseInt();
  }
  
  //start the collecting phase
  //reset pin high not running not sending
  static unsigned long last_sample_time;
  if((runCheck == 8) && (running == 0) && (sending == 0))
  {
    Serial.println("Starting data collection");
    running = 1;
    last_sample_time = micros();

  }

  //if the buffer has been filled 
  //move to sending
  if (x>=30000)
  {
    Serial.println("Data collection complete");
    running =0;
    sending =1;
    x = 0;
    
  }

  //collecting reads pin 25
  if (((micros() - last_sample_time) >= SAMPLE_INTERVAL) && (running == 1)) { 
        last_sample_time += SAMPLE_INTERVAL;  // note 2

      //read analog pin 25
        val = analogRead(25);//microphone one 
        data[x] = val; //microphone one 
        x= x+1;
      
  }

  //sending 
  //wifi transmission
  if (sending == 1)
  {
    Serial.println("Starting Json transmission");

    // make sure the device is still connected
    if(client.connected())
    {
      //initialize the json array
      StaticJsonDocument<30000*sizeof(uint16_t)>doc;
      JsonArray jsonArray = doc.to<JsonArray>();

      //add the collected data to the json
      for(int i=0; i<1000; i++)
      {
        jsonArray.add(data[i]);
      }

      //convert the information tp json format
      size_t bufferSize = measureJson(doc); // Get the size of the JSON object
      char *jsonBuffer = (char *)malloc(bufferSize); // Dynamically allocate memory
      if(!jsonBuffer)
      {
        Serial.println("ERROR");
      }
      Serial.println(jsonArray);
      serializeJson(jsonArray, jsonBuffer);

      //send the information
      // client.println(jsonBuffer);
      //confirmation message
      Serial.println("Json sent");
      free(jsonBuffer);


    // } uncomment for serial recording
    // //mic one data
    // for(int i = 0; i<30000; i++)
    // {
    //      Serial.println(data[i]);
    //      //Serial.flush();
    //      //delayMicroseconds();//delay
    // }

  //   //mic two data
  //   // for(int i = 0; i<20000; i++)
  //   // {
  //   //      Serial.println(data2[i]);
  //   //      //Serial.flush();
  //   //      //delayMicroseconds();//delay
  //   // }
    
    Serial.println("Complete");
    sending = 0;
    
  }



}