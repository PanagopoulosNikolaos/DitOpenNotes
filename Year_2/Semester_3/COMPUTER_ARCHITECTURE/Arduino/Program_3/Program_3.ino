// Temperature-controlled LED system with three-level threshold
// Prompts for max temperature every 10 seconds
// Low (≤80°C): green LED bright, red LED off
// Mid (80-90°C): green LED medium, red LED off
// High (>90°C): red LED bright, green LED off

int gLed = 7;             // PWM pin for green LED (analog brightness control)
int rLed = 8;             // Digital pin for red LED
const unsigned long interval = 10000UL; // Prompt interval: 10 seconds
unsigned long lastPrompt = 0;

const int lowThreshold = 80;
const int highThreshold = 90;

void setup() {
    Serial.begin(9600);
    Serial.setTimeout(3000); // Set timeout for parseInt (milliseconds)
    pinMode(rLed, OUTPUT);
    pinMode(gLed, OUTPUT);
    // Initialize LEDs to off state
    digitalWrite(rLed, LOW);
    analogWrite(gLed, 0);
}

void loop() {
    unsigned long now = millis();

    // Display prompt every 10 seconds
    if (now - lastPrompt >= interval) {
        lastPrompt = now;
        Serial.println("Enter the max temperature in Celsius:");
    }

    // Process temperature input when available
    if (Serial.available() > 0) {
        int maxTemp = Serial.parseInt();
        Serial.print("Got: ");
        Serial.println(maxTemp);

        if (maxTemp <= lowThreshold) {
            // Low temperature: green bright, red off
            analogWrite(gLed, 255);
            digitalWrite(rLed, LOW);
        } else if (maxTemp > highThreshold) {
            // High temperature: red bright, green off
            analogWrite(gLed, 0);
            digitalWrite(rLed, HIGH);
        } else {
            // Mid temperature: green medium brightness, red off
            analogWrite(gLed, 128); // 50% brightness
            digitalWrite(rLed, LOW);
        }

        // Clear remaining characters from serial buffer
        while (Serial.available() > 0) Serial.read();
    }
}
