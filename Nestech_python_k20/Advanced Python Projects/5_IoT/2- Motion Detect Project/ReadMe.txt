Required Hardware
Raspberry Pi (any model)
PIR sensor module
Breadboard
Jumper wires
Wiring


1 Connect the VCC pin of the PIR sensor module to the 5V pin of the Raspberry Pi.
2 Connect the GND pin of the PIR sensor module to the GND pin of the Raspberry Pi.
3 Connect the OUT pin of the PIR sensor module to any GPIO pin of the Raspberry Pi (e.g. GPIO 17).




+-----------------------+      +--------------+
| PIR Sensor Module      |      | Raspberry Pi |
|                       |      |              |
| +------+   +------+  |      | +-----+      |
| | VCC  +---+ 5V   |  |      | | 5V  |      |
| +------+   +------+  |      | +-----+      |
|                       |      |              |
| +------+   +------+  |      | +-----+      |
| | GND  +---+ GND  |  |      | | GND |      |
| +------+   +------+  |      | +-----+      |
|                       |      |              |
| +------+   +------+  |      | +-----+      |
| | OUT  +---+ GPIO |<-+------+ | 17  |      |
| +------+   +------+  |      | +-----+      |
+-----------------------+      +--------------+

4 Make sure to install :
		sudo apt-get install python3-gpiozero

5 Use the code provided in this section!

6 run the file 
