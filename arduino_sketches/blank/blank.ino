
#include <SoftwareSerial.h>
#define txPin 3                                         //define pins used for software serial for sonar (Not Connected)
#define rxPin 2                                         //Connect to TX of the sensor
SoftwareSerial mySerial(rxPin, txPin);                  //Defines the Software Serial Port

int g;
void setup() {
  // Set the data rate for the serial terminal
  Serial.begin(9600);
  mySerial.begin(9600);
}

void loop() {
  if (mySerial.available() > 0) {
    g = mySerial.parseInt();
    Serial.println(g);
  }

}
