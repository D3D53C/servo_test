import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

P = GPIO.PWM(7, 50)
P.start(7.5)
try:
    while True:
        P.ChangeDutyCicle(0.5)
        time.sleep(2)
        P.ChangeDutyCicle(1.5)
        time.sleep(2)
        P.ChangeDutyCicle(2.5)
        time.sleep(3)
except:

    print ("Stop")
    pass
