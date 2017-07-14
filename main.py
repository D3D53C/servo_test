from servo import Servo as Servo
import time

class Main:
    def __init__(self):
        self.servo = Servo(3,50,500,2500,180)
        main()
    def main(self):
        while True:
            servo.change_position(0)
            print("0 Degrees")
            time.sleep(2)
            servo.change_position(90)
            print("90 Degrees")
            time.sleep(2)
            servo.change_position(180)
            print ("180 Degrees")
            time.sleep(5)
