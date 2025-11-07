# Computer Architecture - Arduino Projects

## Program_1: LED Blink with Serial Output

A simple Arduino sketch that blinks the built-in LED on an Arduino Uno while sending status messages to the serial monitor.

### Requirements

- Arduino Uno microcontroller
- USB cable (Type A to Type B)
- Arduino CLI installed
- Linux system with proper USB permissions

### Setup Instructions

#### 1. Install Arduino CLI

```bash
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
```

Add the bin directory to your PATH:
```bash
export PATH="$PATH:$HOME/Documents/University_Code/Semester_3/COMPUTER_ARCHITECTURE/bin"
```

#### 2. Install Arduino AVR Platform

```bash
sudo arduino-cli core install arduino:avr
```

This installs the necessary compiler, tools, and libraries for Arduino Uno development.

#### 3. Connect Your Arduino

Connect your Arduino Uno to your computer via USB cable. Verify the connection:

```bash
arduino-cli board list
```

You should see output similar to:
```
Port         Protocol Type              Board Name  FQBN            Core
/dev/ttyACM0 serial   Serial Port (USB) Arduino Uno arduino:avr:uno arduino:avr
```

### Building and Uploading

#### Compile the Sketch

```bash
cd Program_1
arduino-cli compile --fqbn arduino:avr:uno Program_1.ino
```

#### Upload to Arduino

```bash
sudo arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno Program_1.ino
```

**Note:** `sudo` is required for USB serial port access. Alternatively, you can add your user to the `dialout` group:
```bash
sudo usermod -a -G dialout $USER
```
Then log out and back in.

### Program Behavior

- **LED**: Blinks every 2 seconds (1 second ON, 1 second OFF)
- **Serial Output**: Prints "LED ON" and "LED OFF" messages at 9600 baud

### Viewing Serial Output

To see the serial messages in real-time:

```bash
sudo arduino-cli monitor -p /dev/ttyACM0 --config baudrate=9600
```

### Troubleshooting

**Error: "main file missing from sketch"**
- Ensure the sketch folder name matches the `.ino` filename (e.g., `Program_1` folder contains `Program_1.ino`)

**Error: "Platform 'arduino:avr' not found"**
- Run: `sudo arduino-cli core install arduino:avr`

**Error: "Permission denied" on `/dev/ttyACM0`**
- Run upload command with `sudo`, or add your user to the `dialout` group as shown above

**Arduino not detected**
- Check USB cable connection
- Try a different USB port
- Run: `arduino-cli board list` to verify detection
