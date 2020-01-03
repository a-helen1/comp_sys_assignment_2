const int anPin = 0; // use analog pin 0
long anVolt, mm;


void setup() {
  Serial.begin(9600);

}

void read_sensor() {
   anVolt = analogRead(anPin); // read raw voltage
   mm = anVolt * 5; // convert adc value to mm
}

void loop() {
  read_sensor();
  {Serial.println(mm); // use serial print instad of write to send mm as a string instead of byte
  delay(1000); // one second wait between readings
  }
 }
