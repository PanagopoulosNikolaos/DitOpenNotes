#!/usr/bin/env python3
import serial
import time

def main():
    # Establish serial connection
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        print("Connected to Arduino.")
    except serial.SerialException as e:
        print(f"Could not connect to Arduino: {e}")
        print("Make sure the Arduino is connected and the port is correct.")
        return

    time.sleep(2)  # Delay for establishing connection

    print("Waiting for Arduino prompt...")
    print("The Arduino will prompt for temperature values every 10 seconds.")
    
    # Clear any initial data in the buffer
    ser.flushInput()

    try:
        while True:
            # Read all available data from Arduino
            while ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    print(f"Arduino: {line}")
                
                # Check if this is the temperature prompt
                if "Enter the max temperature in Celsius:" in line:
                    # Prompt user for temperature
                    temp_input = input("Enter temperature value to send to Arduino: ")
                    
                    # Validate input is a number
                    try:
                        temp_value = int(temp_input)
                        # Send the temperature value to Arduino
                        ser.write(f"{temp_value}\n".encode())
                        print(f"Sent temperature: {temp_value}°C to Arduino")
                    except ValueError:
                        print("Please enter a valid integer temperature value.")
                        continue
            
            time.sleep(0.1)  # Delay between reads
            
    except KeyboardInterrupt:
        print("\nClosing connection...")
        ser.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
