from servo import Servo as Servo1
import time
servo = Servo1(11,50,2500,12000,180)
while True:
    servo.change_position(180)
    time.sleep(2)
    servo.change_position(90)
    time.sleep(2)
    servo.change_position(0)
    time.sleep(2)