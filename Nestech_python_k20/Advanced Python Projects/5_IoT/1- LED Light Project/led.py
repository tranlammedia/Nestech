import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pins
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

# Turn on the LEDs
GPIO.output(17, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)

# Wait for 2 seconds
time.sleep(2)

# Turn off the LEDs
GPIO.output(17, GPIO.LOW)
GPIO.output(18, GPIO.LOW)

# Clean up the GPIO pins
GPIO.cleanup()
