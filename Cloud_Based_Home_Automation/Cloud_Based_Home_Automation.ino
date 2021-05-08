"""
@authors: Shagun Chauhan
Project: Cloud Based Home Automation
"""

/*
    We have downloaded Blynk library from here:
      https://github.com/blynkkk/blynk-library/releases/latest
*/

#define BLYNK_PRINT Serial  // Defines the object that is used for printing

#include <ESP8266WiFi.h>  //This library provides ESP8266 specific Wi-Fi routines that we are calling to connect to the network.
#include <BlynkSimpleEsp8266.h> //This header file is part of the Blynk library.

char auth[] = "################################"; //We got this Auth Token in Gmail when we signin Blynk app with oour Gmail ID

// Our WiFi credentials.We can Set password to "" for open networks.
char ssid[] = "test"; //We have entered our WIFI Name
char pass[] = "test";//We have entered our WIFI Password

void setup()
{
  // Debug console
  // Putting our setup code here, to run once:
  Serial.begin(9600); // See the connection status in Serial Monitor
  pinMode(D1,OUTPUT); //Nodemcu PIN D1 having the output for Relay1
  pinMode(D2,OUTPUT); //Nodemcu PIN D2 having the output for Relay2
  pinMode(D3,OUTPUT); //Nodemcu PIN D3 having the output for Relay3

  digitalWrite(D1,HIGH);  //Here HIGH means Relay1 is ON
  digitalWrite(D2,HIGH);  //Here HIGH means Relay1 is ON
  digitalWrite(D3,HIGH);  //Here HIGH means Relay1 is ON
  
  Blynk.begin(auth, ssid, pass);  // Here our Nodemcu connects to the Blynk Cloud.
  // We can also specify server:
  //Blynk.begin(auth, ssid, pass, "blynk-cloud.com", 8442);
  //Blynk.begin(auth, ssid, pass, IPAddress(192,168,1,100), 8442);
}

void loop()
{
  // Putting our main code here, to run repeatedly:
  Blynk.run();  // All the Blynk Magic happens here...
}
