# Import the required libraries
import RPi.GPIO as GPIO
import time

# List of duty cycles to use for servo movement
control = [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]

# GPIO pin connected to the servo
servo_pin = 4

# Configure GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Initialize PWM for the servo on pin 4 at 50Hz
pwm = GPIO.PWM(servo_pin, 50)

# Start the PWM with initial duty cycle, setting the servo at 0 degree
pwm.start(2.5)

try:
    # Main control loop
    while True:
        # Move the servo through the specified duty cycles
        for duty_cycle in control:
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(1)
            print(duty_cycle)
        
        # Move the servo back through the specified duty cycles
        for duty_cycle in reversed(control[:-1]):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(1)
            print(duty_cycle)

# Handle keyboard interrupt to clean up GPIO settings
except KeyboardInterrupt:
    GPIO.cleanup()