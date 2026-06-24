# Program 2: External LED Blink with Counter

Arduino program that blinks an external LED and counts up to 50 blinks.

## Functionality

- Blinks external LED on pin 9 every second
- Displays current count on serial monitor
- Stops after reaching 50 blinks

## Upload Instructions

```bash
arduino-cli compile --fqbn arduino:avr:uno Program_2.ino
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno Program_2.ino
```

## Components Required

- Arduino Uno
- LED
- 220Ω resistor
- Jumper wires
- Breadboard

## Circuit

Connect LED to pin 9 with resistor to ground.

## Serial Monitor

Open serial monitor at 9600 baud to see LED status and count.
