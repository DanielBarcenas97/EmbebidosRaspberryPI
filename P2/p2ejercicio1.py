from bluedot import BlueDot
from signal import pause

def saludo():
	print("Hola Mundo")

def despedida():
	print("Hasta Pronto")

bd = BlueDot()
bd.when_pressed = saludo
bd.when_released = despedida

pause()
