import gpiozero as GPIO
import time


test = GPIO.PWMLED(18)

"""
for b in range(101):
	test.value = b/100.0
	time.sleep(0.01)
"""


test.value = 0


