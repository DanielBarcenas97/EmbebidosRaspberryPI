#Control de motor

from gpiozero import Motor
from time import sleep

motor = Motor(forward=4,backward=14)

while True:
	Motor.forward()
	sleep(5)
	motor.backward()
	sleep(5)
