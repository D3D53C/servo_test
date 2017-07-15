import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

P = GPIO.PWM(3, 50)
P.start(7.5)
while True:
        P.ChangeDutyCycle(0.5)
        time.sleep(2)
        P.ChangeDutyCycle(1.5)
        time.sleep(2)
        P.ChangeDutyCycle(2.5)
        time.sleep(3)
