# Description: This program will read the analog value from the potentiometer
# and use that value to control the duty cycle of the PWM signal to the servo

# Import the libraries
import RPi.GPIO as GPIO
import ADC0834
from time import sleep

# GPIO and PWM Setup
GPIO.setmode(GPIO.BCM)
pwmPin = 4
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50)
pwm.start(0)
ADC0834.setup()

# Main Loop - Read the analog value and set the duty cycle
try:
    while True:
        analogVal = ADC0834.getResult(0)        # Read the analog value
        pwmPercent = 10/255*(analogVal)     # Convert to percent duty cycle
        print(pwmPercent)
        pwm.ChangeDutyCycle(pwmPercent)         # Set the duty cycle
        sleep(.1)

# Reset by pressing CTRL + C
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Clean')