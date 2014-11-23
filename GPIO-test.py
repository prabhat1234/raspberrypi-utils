import RPi.GPIO as GPIO
import time
import sys


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)

num = len(sys.argv)
if num > 1:
    led = sys.argv[1]
    GPIO.output(led,True)
    time.sleep(5.0)
    GPIO.output(led, False)
else:
    print "Blinking all led's"
    for i in range (0, 5)
        GPIO.output(3,True)
        time.sleep(5.0)
        GPIO.output(3, False)

        GPIO.output(3,True)
        time.sleep(5.0)
        GPIO.output(3,False)

        GPIO.output(3,True)
        time.sleep(5.0)
        GPIO.output(3,False)
    print "Switching OFF led's"

