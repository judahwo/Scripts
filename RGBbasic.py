import RPi.GPIO as GPIO 
from time import sleep

GPIO.setmode(GPIO.BOARD)

rPin = 37
gPin = 35
bPin = 33

GPIO.setup(rPin,GPIO.OUT)
GPIO.setup(gPin,GPIO.OUT)
GPIO.setup(bPin,GPIO.OUT)

GPIO.output(rPin,0)
GPIO.output(gPin,0)
GPIO.output(bPin,0)
sleep(5)
GPIO.cleanup()
