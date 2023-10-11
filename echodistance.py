# Purpose: Measure distance using an ultrasonic sensor

# Import libraries
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Pin assignments
trigPin = 23
echoPin = 24

# Pin setup
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try:
    while True:
        # Send echo pulses
        GPIO.output(trigPin, 0)
        time.sleep(2E-6)
        GPIO.output(trigPin, 1)
        time.sleep(10E-6)
        GPIO.output(trigPin, 0)

        # Wait for echo
        while GPIO.input(echoPin) == 0:
            pass
        echoStartTime = time.time()
        
        while GPIO.input(echoPin) == 1:
            pass
        echoStopTime = time.time()

        # Calculate distance
        ptt = echoStopTime - echoStartTime
        distance = 6749.2 * ptt
        print(round(distance, 1), 'Inches')
        time.sleep(.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Clean')