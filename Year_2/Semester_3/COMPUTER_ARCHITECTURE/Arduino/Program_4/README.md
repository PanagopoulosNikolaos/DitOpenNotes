# Program 4: Ultrasonic Distance Sensor

Arduino program that measures distance using an HC-SR04 ultrasonic sensor with enhanced accuracy features.

## Functionality

- Measures distance using ultrasonic sensor
- Median filtering to reject outliers (7 samples)
- Temperature-compensated sound speed calculation
- Timeout handling for out-of-range detection
- Updates ~4 times per second

## Upload Instructions

```bash
arduino-cli compile --fqbn arduino:avr:uno Program_4.ino
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno Program_4.ino
```

## Components Required

- Arduino Uno
- HC-SR04 ultrasonic sensor
- Jumper wires
- Breadboard

## Circuit

- TRIGGER pin → Arduino pin 3
- ECHO pin → Arduino pin 2
- VCC → 5V
- GND → GND

## Serial Monitor

Open serial monitor at 9600 baud to see distance measurements in centimeters.

## Python Script

Run `main_execute.py` to read and log distance measurements from the Arduino.
