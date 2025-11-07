void setup() {
  // Initialize serial communication at 9600 baud
  Serial.begin(9600);
  
  // Configure built-in LED pin as output
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // Turn LED on
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("LED ON");
  delay(1000);
  
  // Turn LED off
  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("LED OFF");
  delay(1000);
}
