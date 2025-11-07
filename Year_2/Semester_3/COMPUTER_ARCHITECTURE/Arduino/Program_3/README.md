# Program 3: Temperature Controlled LED

This program reads a temperature value from the serial input and controls two LEDs based on the value:
- If temperature ≤ 85°C: Green LED (pin 7) turns ON, Red LED (pin 8) turns OFF
- If temperature > 85°C: Red LED (pin 8) turns ON, Green LED (pin 7) turns OFF

## How to Use

1. Upload the Program_3.ino to your Arduino:
   ```bash
   arduino-cli compile --fqbn arduino:avr:uno Program_3.ino
   arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno Program_3.ino
   ```

2. Run the Python script to send temperature values:
   ```bash
   python send_temp.py
   ```

3. Follow the prompts to enter temperature values.

## Components Required

- Arduino Uno
- Green LED connected to pin 7
- Red LED connected to pin 8
- 220Ω resistors for each LED
- Jumper wires
- Breadboard

## Circuit Diagram

Connect as follows:
- Green LED to pin 7 with resistor to ground
- Red LED to pin 8 with resistor to ground
