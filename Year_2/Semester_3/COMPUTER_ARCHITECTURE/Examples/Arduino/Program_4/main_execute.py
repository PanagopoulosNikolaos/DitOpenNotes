import serial
import time
import sys

def connectToArduino(port=None, baud_rate=9600):
    """Establishes a serial connection to the Arduino device.

    Args:
        port (str, optional): Target serial port path. Defaults to None.
        baud_rate (int, optional): Baud communication rate. Defaults to 9600.

    Returns:
        serial.Serial: Active serial connection object.

    Raises:
        RuntimeError: If connection fails across all scanned candidate ports.
    """
    if port is None:
        ports = ['/dev/ttyUSB0', '/dev/ttyACM0', '/dev/ttyUSB1', '/dev/ttyACM1']
        for p in ports:
            try:
                ser = serial.Serial(p, baud_rate, timeout=1)
                print(f"Connected to Arduino on {p}")
                return ser
            except serial.SerialException:
                continue
        raise RuntimeError("Could not connect to Arduino on any common port")
    else:
        return serial.Serial(port, baud_rate, timeout=1)


def readDistance(ser):
    """Reads and parses a distance measurement from the Arduino serial stream.

    Args:
        ser (serial.Serial): Active serial connection instance.

    Returns:
        int | None: Distance in centimeters if valid, otherwise None.
    """
    try:
        line = ser.readline().decode('utf-8').strip()
        if "Distance:" in line:
            if "out of range" in line:
                print("Sensor reading: out of range")
                return None
            elif "cm" in line:
                distance_str = line.split("Distance:")[1].split("cm")[0].strip()
                try:
                    distance = float(distance_str)
                    return round(distance)
                except ValueError:
                    return None
        return None
    except UnicodeDecodeError:
        return None
    except Exception:
        return None


def getSingleDistance(ser):
    """Fetches a single distance measurement from the sensor.

    Args:
        ser (serial.Serial): Active serial connection instance.

    Returns:
        int | None: Measured distance value or None on failure.
    """
    print("Getting distance...")
    distance = readDistance(ser)
    if distance is not None:
        print(f"Distance: {distance} cm")
        return distance
    else:
        print("Could not get distance reading. Please try again.")
        return None


def continuousDistance(ser, interval=10):
    """Polls distance measurements continuously at a specified interval.

    Args:
        ser (serial.Serial): Active serial connection instance.
        interval (int, optional): Polling interval in seconds. Defaults to 10.

    Returns:
        None.
    """
    print(f"Starting continuous distance measurement (every {interval} seconds). Press Ctrl+C to stop.")
    try:
        while True:
            distance = readDistance(ser)
            if distance is not None:
                print(f"Distance: {distance} cm")
            else:
                print("Could not get distance reading.")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nContinuous measurement stopped.")
        return


def main():
    """Runs interactive command-line interface for ultrasonic sensor measurement.

    Args:
        None.

    Returns:
        None.
    """
    print("Ultrasonic Distance Measurement Program")
    print("Connecting to Arduino...")
    
    try:
        ser = connectToArduino()
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
                getSingleDistance(ser)
            elif choice == 0:
                print("Shutting down program...")
                ser.close()
                sys.exit(0)
            elif choice == 2:
                continuousDistance(ser, 10)
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
