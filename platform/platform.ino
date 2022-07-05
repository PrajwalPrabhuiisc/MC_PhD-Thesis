#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

// Replace with your network credentials
const char* ssid = "Galaxy M211BF1";         
const char* password = "pufy3612";

ESP8266WebServer server(80);   //instantiate server at port 80 (http port)

String page = ""; //For the Web Server
String page2="";  //For updating Status of motor 1
void setup(void)
{
  //the HTML of the web page
  page = "<center><h1>Motor Control Web Server</h1><body><p><a href=\"Forward\"><button>Forward</button></a><p><a href=\"Backward\"><button>Backward</button></a></p><a href=\"Stop\"><button>Stop</button></a></p></body></center>";
 
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

 void Forward() 
 {
    digitalWrite(D2,HIGH);
    digitalWrite(D1,LOW);
    page2="<center><p> motor 1 Status : Forward </p></center>";
    server.send(200,"text/html", page+page2);
    Serial.print('forward');
    delay(200);
  }
  
   void Backward()
  {
    page2="<center><p> motor 1 Status : Backward</p></center>";
    server.send(200, "text/html", page+page2);
    digitalWrite(D1, HIGH);
    digitalWrite(D2,LOW);
    Serial.print('back');
    delay(200); 
  }
