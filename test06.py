from servo import Servo as Servo
import time

servo = Servo(7,50,2500,12500,180)

while True:
    servo.change_position(180)
    time.sleep(2)
    servo.change_position(90)
    time.sleep(2)
    servo.change_position(0)
    time.sleep(2)