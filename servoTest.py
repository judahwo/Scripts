# Import the required libraries
import RPi.GPIO as GPIO
import time

# GPIO pin connected to the servo
servo_pin = 4

# Configure GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Initialize PWM for the servo on pin 4 at 50Hz
pwm = GPIO.PWM(servo_pin, 50)

# Start the PWM with an initial duty cycle, setting the servo at 0 degree
pwm.start(0)

# Function to set the servo angle
def set_servo_angle(angle):
    # Calculate duty cycle from angle
    duty_cycle = (angle / 18) + 2.5
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Allow the servo to move to the set angle
    pwm.ChangeDutyCycle(0)  # Stop the servo

try:
    # Request an angle from the user
    angle = float(input("Enter the angle between 0 and 180 degrees: "))
    
    # Ensure the angle is within 0-180
    if 0 <= angle <= 180:
        set_servo_angle(angle)
    else:
        print("Invalid input. Please enter an angle between 0 and 180 degrees.")

# Handle keyboard interrupt to clean up GPIO settings
except KeyboardInterrupt:
    pass

# Clean up GPIO settings
GPIO.cleanup()
