# Program 1: Built-in LED Blink

Basic Arduino program that blinks the built-in LED on and off every second.

## Functionality

- Turns built-in LED ON for 1 second
- Turns built-in LED OFF for 1 second
- Sends status to serial monitor

## Upload Instructions

```bash
arduino-cli compile --fqbn arduino:avr:uno Program_1.ino
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno Program_1.ino
```

## Components Required

- Arduino Uno (built-in LED on pin 13)
- USB cable

## Serial Monitor

Open serial monitor at 9600 baud to see LED status messages.
