import RPi.GPIO as GPIO
import time

ipin = 20

GPIO.setmode(GPIO.BCM)

GPIO.setup(ipin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 1

while count < 5:
    input_state = GPIO.input(ipin)
    if not input_state:
        print "Button pressed #" + str(count)
        count += 1
        time.sleep(1)
