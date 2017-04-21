import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 1

while count < 5:
	input_state = GPIO.input(18)
	if input_state == False:
		print "gedrueckt Nr. " + str(count)
		count += 1
		time.sleep(0.2)
