To create a project with two LEDs on a Raspberry Pi, you will need:

Raspberry Pi (any version will do)
Two LEDs (different colors if possible)
Two 220 ohm resistors
Jumper wires
Breadboard (optional)


Here are the steps to create the project:

1 - Connect the negative (shorter) leg of each LED to a GPIO pin on the Raspberry Pi. It is recommended to use GPIO pins 17 and 18 as they are next to each other.

2 - Connect the positive (longer) leg of each LED to a 220 ohm resistor.

3 - Connect the other end of the resistor to the ground (GND) pin on the Raspberry Pi.

4 - Open the Terminal on your Raspberry Pi and type the following command to install the GPIO library:


		sudo apt-get update
		sudo apt-get install rpi.gpio


5 - Create a new Python file on your Raspberry Pi by typing the following command in the Terminal:

		nano led.py


6 - and copy the code in this section.

7 - Save the led.py file

8 - Run the led.py file by typing the following command in the Terminal:

		python led.py
