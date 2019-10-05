from gpiozero import LED
from time import sleep
from signal import pause

red = LED(5)
yellow = LED(6)
green = LED(13)

while True:
	red.on()
	sleep(3)
	red.off()
	yellow.on()
	sleep(1)
	yellow.off()
	yellow.on()
	sleep(1)
	yellow.off()
	green.on()
	sleep(3)
	green.off()


