from gpiozero import LEDBoard
from time import sleep
from signal import pause
from bluedot import BlueDot




def nombres(pos):
	if pos.top:
		leds.value(1,1,0,0,1,1,0)
		sleep(1)
		leds.value(0,1,1,0,1,1,1)
		sleep(1)
		leds.value(1,1,1,0,0,0,0)
		sleep(1)
		leds.value(1,1,1,1,0,0,1)
	elif pos.bottom:
		leds.value(0,1,1,1,1,1,1)
		sleep(1)
		leds.value(0,1,1,0,1,1,1)
		sleep(1)
		leds.value(0,1,1,0,1,1,1)
		sleep(1)
		leds.value(0,1,1,0,0,0,0)

leds=LEDBoard(2,3,4,17,27,22,10)
bd=BlueDot()
bd.when_pressed=nombres
pause()
