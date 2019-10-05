#Carrito a control remoto con raspberryPI3

from bluedot import BlueDot
from gpiozero import Robot
from signal import pause

bd = BlueDot()
robot = Robot(left=(4, 14), right=(17, 18))

def move(pos):
	if pos.top:
		robot.forward()
		print("Forward")
	elif pos.bottom:
		robot.backward(pos.distance)
		print("Backward")
	elif pos.left:
		robot.left(pos.distance)
		print("Left")
	elif pos.right:
		robot.right(pos.distance)
		print("Right")

bd.when_pressed = move
bd.when_moved = move
bd.when_released = robot.stop
pause()
