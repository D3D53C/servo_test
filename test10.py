import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

P1 = GPIO.PWM(3, 50)
P2 = GPIO.PWM(5, 50)
P3 = GPIO.PWM(7, 50)
P4 = GPIO.PWM(8, 50)
P5 = GPIO.PWM(10, 50)

P1.start(7.5)
P2.start(7.5)
P3.start(7.5)
P4.start(7.5)
P5.start(7.5)

while True:
    P1.ChangeDutyCycle(0.5)
    P2.ChangeDutyCycle(0.5)
    P3.ChangeDutyCycle(0.5)
    P4.ChangeDutyCycle(0.5)
    P5.ChangeDutyCycle(0.5)

    time.sleep(2)
    P1.ChangeDutyCycle(1.5)
    P2.ChangeDutyCycle(1.5)
    P3.ChangeDutyCycle(1.5)
    P4.ChangeDutyCycle(1.5)
    P5.ChangeDutyCycle(1.5)

    time.sleep(2)
    P1.ChangeDutyCycle(2.5)
    P2.ChangeDutyCycle(2.5)
    P3.ChangeDutyCycle(2.5)
    P4.ChangeDutyCycle(2.5)
    P5.ChangeDutyCycle(2.5)
    time.sleep(3)
