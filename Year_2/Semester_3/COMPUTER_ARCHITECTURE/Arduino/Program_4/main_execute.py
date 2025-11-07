import serial
import time
import sys

# Configure the serial connection
def connect_to_arduino(port=None, baud_rate=9600):
    """
    Connect to Arduino via serial.
    Auto-detects port if not specified.
    """
    if port is None:
        # Try common ports
        ports = ['/dev/ttyUSB0', '/dev/ttyACM0', '/dev/ttyUSB1', '/dev/ttyACM1']
        for p in ports:
            try:
                ser = serial.Serial(p, baud_rate, timeout=1)
                print(f"Connected to Arduino on {p}")
                return ser
            except serial.SerialException:
                continue
        raise Exception("Could not connect to Arduino on any common port")
    else:
        return serial.Serial(port, baud_rate, timeout=1)

def read_distance(ser):
    """
    Read distance measurement from Arduino.
    Returns distance in cm or None if invalid.
    """
    try:
        # Read a line from serial
        line = ser.readline().decode('utf-8').strip()
        if "Distance:" in line:
            if "out of range" in line:
                print("Sensor reading: out of range")
                return None
            elif "cm" in line:
                # Extract the numeric value
                distance_str = line.split("Distance:")[1].split("cm")[0].strip()
                try:
                    distance = float(distance_str)
                    return round(distance)  # Returns as integer for consistency
                except ValueError:
                    return None
        return None
    except UnicodeDecodeError:
        return None
    except Exception:
        return None

def get_single_distance(ser):
    """
    Get single distance reading.
    """
    print("Getting distance...")
    distance = read_distance(ser)
    if distance is not None:
        print(f"Distance: {distance} cm")
        return distance
    else:
        print("Could not get distance reading. Please try again.")
        return None

def continuous_distance(ser, interval=10):
    """
    Continuous distance readings at specified interval.
    """
    print(f"Starting continuous distance measurement (every {interval} seconds). Press Ctrl+C to stop.")
    try:
        while True:
            distance = read_distance(ser)
            if distance is not None:
                print(f"Distance: {distance} cm")
            else:
                print("Could not get distance reading.")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nContinuous measurement stopped.")
        return

def main():
    print("Ultrasonic Distance Measurement Program")
    print("Connecting to Arduino...")
    
    try:
        ser = connect_to_arduino()
        time.sleep(2)  # Delay for establishing connection
        
        while True:
            print("\nOptions:")
            print("1 - Get distance once")
            print("0 - Shutdown program")
            print("2 - Continuous distance measurement (every 10 seconds)")
            
            try:
                choice = int(input("Enter your choice (1, 0, or 2): "))
            except ValueError:
                print("Invalid input. Please enter 0, 1, or 2.")
                continue
            
            if choice == 1:
                get_single_distance(ser)
            elif choice == 0:
                print("Shutting down program...")
                ser.close()
                sys.exit(0)
            elif choice == 2:
                continuous_distance(ser, 10)
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
