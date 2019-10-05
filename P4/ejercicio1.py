import Adafruit_DHT
import time
import os
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

file= open("datos.txt", "w")

while True:
	humedad, temperatura = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
	if humedad is not None and temperatura is not None:
		print("Temperatura={0:0.1f}C Humedad = {1:01f}%".format(temperatura,humedad))
		file.write("Temperatura={0:0.1f}C Humedad = {1:01f}% \n".format(temperatura,humedad))
	else:
		print("Falla el sensor")
	time.sleep(3);

f.close()
