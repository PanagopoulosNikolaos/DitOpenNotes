// External LED blinking with counter
const int ledPin = 9;  // External LED pin
int count = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Turn LED on and display count
  digitalWrite(ledPin, HIGH);
  Serial.print("LED ON - Count: ");
  Serial.println(count);
  delay(1000);

  // Turn LED off and display count
  digitalWrite(ledPin, LOW);
  Serial.print("LED OFF - Count: ");
  Serial.println(count);
  delay(1000);

  count++;
  if (count > 50) {
    Serial.println("Done counting!");
    while (true);  // Stop execution
  }
}
