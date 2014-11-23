import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

while True:
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup(3,GPIO.OUT)

    def my_handler(channel):
        GPIO.output(3,True)

    def my_handler1(channel):
        GPIO.output(3, False)


    GPIO.add_event_detect(11, GPIO.FALLING, callback=my_handler)
    GPIO.add_event_detect(12, GPIO.FALLING, callback=my_handler1)


    try:
        GPIO.wait_for_edge(11, GPIO.FALLING)
    except KeyboardInterrupt:
        GPIO.cleanup()

    try:
        GPIO.wait_for_edge(12, GPIO.FALLING)
    except KeyboardInterrupt:
        GPIO.cleanup()
