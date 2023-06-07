import time
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)
bcm_pin = 16
GPIO.setup(bcm_pin, GPIO.IN )

while True: 
    voltage = GPIO.input(bcm_pin)
    print("Moisture: ", voltage)
    time.sleep(1)
    voltage = GPIO.input(bcm_pin)
