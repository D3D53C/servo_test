import RPi.GPIO as gpio

pin = 3
frequenz = 50

gpio.setmode(gpio.BOARD)
gpio.setup(pin ,gpio.OUT)
pwmpin = gpio.PWM(pin, frequenz)


pwmpin.ChangeDutyCycle(2.5)

