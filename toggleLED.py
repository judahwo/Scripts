from time import sleep
import RPi.GPIO as GPIO

delay = .1
inPin = 40
outPin = 38
LEDstate = 0
buttonState = 1
buttonStateOld = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin,GPIO.OUT)
GPIO.setup(inPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
	while True:
		buttonState = GPIO.input(inPin)
		print(buttonState)
		if buttonState == 1 and buttonStateOld == 0:
			LEDstate = not LEDstate
			GPIO.output(outPin,LEDstate)
		buttonStateOld = buttonState
		sleep(delay)
except KeyboardInterrupt:
	GPIO.cleanup()
	print('GPIO Clean')
