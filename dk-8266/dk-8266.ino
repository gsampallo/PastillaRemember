/*
 * gsampallo.com
 * You need to install ESP8266WiFi, PubSubClient and U8g2lib to compile
 * https://github.com/gsampallo/PastillaRemember
 */
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <U8g2lib.h>

const char* ssid     = "SSD";
const char* password = "PASSWORD";
const char* mqtt_server = "MQTT_SERVER";

//U8g2 Contructor
U8G2_SSD1306_128X32_UNIVISION_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ 16, /* clock=*/ 5, /* data=*/ 4);


u8g2_uint_t offset;     // current offset for the scrolling text
u8g2_uint_t width;      // pixel width of the scrolling text (must be lesser than 128 unless U8G2_16BIT is defined
const char *text = "ROB01 "; // scroll this text from right to left

WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
int value = 0;

int boton = 15;

void setup() {
  u8g2.begin();
  
  Serial.begin(115200);
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    mostrar_texto("Conectando");
    delay(500);
  }
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback); 

  pinMode(boton,INPUT);
}

void reconectar() {
  String clientId = "ESP8266Client-";
  clientId += String(random(0xffff), HEX);
  while(!client.connected()) {   
    
    if (client.connect(clientId.c_str())) {
      Serial.println("conectado a "+String(mqtt_server));
      client.subscribe("MENSAJE");

      mostrar_texto("Conectando"); 

      delay(1000);

      mostrar_texto(" ");       
    } else {
      mostrar_texto("Conectando");
    }
  }
}

void mostrar_texto(String texto) {
  u8g2.clearBuffer();
  u8g2.setFont(u8g2_font_ncenB14_tr);
  u8g2.drawStr(0,20,texto.c_str());
  u8g2.sendBuffer();  
}

boolean alerta = true;

void callback(char* topic, byte* payload, unsigned int length) {
  String tema = String(topic);
  String mensaje = String((char*)payload).substring(0,length);

  if(tema == "MENSAJE") {
    mostrar_texto(mensaje); 
  }

}

void enviar_ok() {
  mostrar_texto("OK");
  delay(200);
  client.publish("PASTILLA", "Tomada");
}

void loop() {
  if (!client.connected()) {
    reconectar();
  }
  client.loop();


  if(digitalRead(boton) == HIGH) {
    enviar_ok();
  }
  

  delay(1);
}