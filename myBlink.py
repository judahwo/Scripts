import RPi.GPIO as GPIO
import time
cont='Y'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
while cont=='Y':
	numBlink=int(input('How many blinks:?'))
	for i in range(0,numBlink):
		GPIO.output(11,1)
		time.sleep(1)
		GPIO.output(11,0)
		time.sleep(1)
	cont=input('Do you wish to continue?: (Y for Yes) ')
GPIO.cleanup()
