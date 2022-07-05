#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

// Replace with your network credentials
const char* ssid = "Galaxy M211BF1";         
const char* password = "pufy3612";
const int trigPin = 14;
const int echoPin = 12;
long duration;
float distanceCm;
float distance1;
#define SOUND_VELOCITY 0.034

ESP8266WebServer server(80);   //instantiate server at port 80 (http port)

String page = ""; //For the Web Server
String page2="";  //For updating Status of motor 1
void setup(void)
{
  //the HTML of the web page
  page = "<center><h1>Lift Control using Web Server</h1><body><p><a href=\"Forward\"><button>Ground Floor</button></a><p><a href=\"Backward\"><button>First Floor</button></a></p><p><a href=\"Left\"><button>Second Floor</button></a></p><a href=\"Stop\"><button>Stop</button></a></p></body></center>";
 
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  pinMode(D2, OUTPUT);   // inputs for motor 1
  pinMode(D1,OUTPUT);
  Serial.begin(115200);     
  WiFi.begin(ssid, password); //begin WiFi connection
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  digitalWrite(LED_BUILTIN,HIGH);     // when connected turns high
  Serial.println("");
  Serial.print("Connected to ");   
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());   //provides IP address
   server.on("/", [](){
    server.send(200, "text/html", page+page2);
  });
  server.on("/Forward",Forward);
  server.on("/Backward",Backward);
  server.on("/Left",Left);
  server.on("/Stop",[](){                              // turns all the motor input pins low
   page2="<center><p> motor 1 Status : Off</p></center>";
  server.send(200,"text/html",page+page2);
    digitalWrite(D2,LOW);
    digitalWrite(D1,LOW);
    delay(200);
  });
  server.begin();
  Serial.println("Web server started!");
}
void loop(void)
{  
     server.handleClient(); 
}

float distance()
{
     digitalWrite(trigPin, LOW);
     delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
     digitalWrite(trigPin, HIGH);
     delay(10);
     digitalWrite(trigPin, LOW);
     duration = pulseIn(echoPin, HIGH);
     distanceCm = duration * SOUND_VELOCITY/2 - 2.5;
     Serial.print("Distance (cm): ");
     Serial.println(distanceCm);
     return distanceCm;
}

void Forward ()
{
  while (true)
  {
    distance1 = distance();
     if (distance1 >= 98.5 && distance1<=99.5)
       {
          digitalWrite(D2,LOW);
          digitalWrite(D1,LOW);
          break;
        }
      else if (distance1<98.5 && distance1 >0)
        {
          digitalWrite(D1,LOW);
          digitalWrite(D2,HIGH);
        }
      else 
        {
          digitalWrite(D2,LOW);
          digitalWrite(D1,LOW);
        }
  }
          page2="<center><p> Lift Status : Lift has reached the Ground Floor </p></center>";
          server.send(200,"text/html", page+page2);
}

void Backward ()
{
  while (true)
  {
    distance1 = distance();
     if (distance1 >= 71 && distance1<=71.5)
       {
          digitalWrite(D2,LOW);
          digitalWrite(D1,LOW);
          break;
        }
      else if (distance1<71 && distance1 >0)
        {
          digitalWrite(D1,LOW);
          digitalWrite(D2,HIGH);
        }
      else if (distance1 >71.5)
        {
          digitalWrite(D1,HIGH);
          digitalWrite(D2,LOW);
        }

      else 
        {
          digitalWrite(D2,LOW);
          digitalWrite(D1,LOW);
        }
  }
          page2="<center><p> Lift Status : Lift has reached the First Floor </p></center>";
          server.send(200,"text/html", page+page2);
}

void Left ()
{
 while (true)
  {
    distance1 = distance();
  if (distance1 >= 38 && distance1<=39)
  {
  digitalWrite(D2,LOW);
  digitalWrite(D1,LOW);
  break;
  }
  else if (distance1>0 && distance1 <38)
  {
  digitalWrite(D2,HIGH);
  digitalWrite(D1,LOW);
  }
  else if (distance1>39)
  {
    digitalWrite(D1,HIGH);
    digitalWrite(D2,LOW);
  } 
  else 
  {
   digitalWrite(D2,LOW);
   digitalWrite(D1,LOW);
   break;
   }
  }
  page2="<center><p> Lift Status : Lift has reached the Second Floor </p></center>";
  server.send(200,"text/html", page+page2);
}
