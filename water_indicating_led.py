import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
moisture_pin = 13
led_pin = 11

GPIO.setup(moisture_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

while True:
    voltage = GPIO.IN
    if voltage == 1:
        GPIO.output(led_pin, GPIO.HIGH)
        print("Dry")
    else:
        GPIO.output(led_pin, GPIO.LOW)
        print("Water")
            
    time.sleep(1)
    voltage = GPIO.input(moisture_pin)
        