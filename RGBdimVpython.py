from vpython import *
import RPi.GPIO as GPIO
from time import sleep

dt = .1

rPin = 37
gPin = 35
bPin = 33

rBut = 11
gBut = 13
bBut = 15

rButState = 1
rButStateOld = 1

gButState = 1
gButStateOld = 1

bButState = 1
bButStateOld = 1

GPIO.setmode(GPIO.BOARD)

GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

GPIO.setup(rBut, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(gBut, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(bBut, GPIO.IN, pull_up_down = GPIO.PUD_UP)

myPWMr = GPIO.PWM(rPin, 100)
myPWMg = GPIO.PWM(gPin, 100)
myPWMb = GPIO.PWM(bPin, 100)

DCr = .9
DCg = .9
DCb = .9

myPWMr.start(int(DCr))
myPWMg.start(int(DCg))
myPWMb.start(int(DCb))

mySphere = sphere(color=color.white, radius = 1, pos = vector(0, 2.5, 0))
myCyl = cylinder(color = color.white, radius = 1, length = 2.5, axis = vector(0, 1, 0))
myBase = cylinder(color = color.white, radius = 1.2, length = .25, axis = vector(0, 1, 0))
myLeg1 = box(pos = vector(-.75, -3, 0), size = vector(.1, 6, .1), color = vector(.2, .2, .2))
myLeg2 = box(pos = vector(.75, -3, 0), size = vector(.1, 6, .1), color = vector(.2, .2, .2))

try:
        while True:
                rate(20)
                rButState = GPIO.input(rBut)
                gButState = GPIO.input(gBut)
                bButState = GPIO.input(bBut)
                print('Button State', rButState, gButState, bButState)
                if rButState == 1 and rButStateOld == 0:
                        DCr = DCr*1.58
                        print('Red Channel Registered')
                        if DCr > 99:
                                DCr = .99
                        myPWMr.ChangeDutyCycle(int(DCr))
                if gButState == 1 and gButStateOld == 0:
                        DCg = DCg*1.58
                        print('Green Channel Registered')
                        if DCg > 99:
                                DCg = .99
                        myPWMg.ChangeDutyCycle(int(DCg))
                if bButState == 1 and bButStateOld == 0:
                        DCb = DCb*1.58
                        print('Blue Channel Registered')
                        if DCb > 99:
                                DCb = .99
                        myPWMb.ChangeDutyCycle(int(DCb))
                rButStateOld = rButState
                gButStateOld = gButState
                bButStateOld = bButState
                print(DCr, DCg, DCb)
                mySphere.color  = vector(DCr/25, DCg/25, DCb/25)
                myCyl.color = vector(DCr/25, DCg/25, DCb/25)
                myBase.color = vector(DCr/25, DCg/25, DCb/25)
                sleep(dt)
except KeyboardInterrupt:
	GPIO.cleanup()
	print()
	print('GPIO Clean')
	print()
