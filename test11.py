from servo import Servo as Servo1
import time

PIN1 = 1;
PIN2 = 2;

servo1 = Servo1(PIN,50,2500,12000,180)
servo2 = Servo2(PIN,50,2500,12000,180)
while True:
	servo1.change_position(180)
	time.sleep(2)
	servo1.STOP()
	servo2.change_position(180)
	time.sleep(2)
	servo2.STOP()
	time.sleep(5)
	servo1.change_position(0)
	time.sleep(2)
	servo1.STOP()
	servo2.change_position(0)
	time.sleep(2)
	servo2.STOP()
	time.sleep(5)
