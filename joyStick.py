# Description: This program reads the analog values from the joystick and the button state
# and prints them to the screen

# Import the libraries  
import RPi.GPIO as GPIO
import ADC0834
import time

# GPIO Setup
GPIO.setmode(GPIO.BCM)
ADC0834.setup()
buttonPin = 21
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP) 

# Main Loop - Read the analog values and button state
try:
    while True:
        analogValX = ADC0834.getResult(0) # Read the analog values
        analogValY = ADC0834.getResult(1) 
        buttonState = GPIO.input(buttonPin) # Read the button state
        print('X Value:', analogValX, 'Y Value:', analogValY, 'Button:', buttonState) 
        time.sleep(.5)
# Reset by pressing CTRL + C
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Clean")