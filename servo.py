
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""servo.py:	Servo class"""

__author__ = "Raphael Kreft & Marc Steinebrunner"
__copyright__ = ""
__version__ = "Development v0.03"
__email__ = "raphaelkreft@gmx.de & marc.steinebrunner@gmail.com"
__status__ = "Dev"

import RPi.GPIO as gpio

class Servo(object):
    def __init__(self,pin):
        self.__init__(self,pin,50,500,2500,180)
    def __init__(self,pin,frequenz):
        self.init(self,pin,frequenz,500,2500,180)
    def __init__(self,pin,operation_angel):
        self.__init__(self,pin,50,500,2500,180)
    def __init__(self, pin, frequenz, PulseRangeMinInUS, PulseRangeMaxInUS, operating_angle):
        gpio.setmode(gpio.BOARD)
        gpio.setup(pin ,gpio.OUT)
        self.frequenz = frequenz
        self.pwmpin = gpio.PWM(pin, frequenz)
        self.PRMin = PulseRangeMinInUS / 1000
        self.PRMax = PulseRangeMaxInUS / 1000
        self.operating_angle = operating_angle

    def get_frequenz(self):
        return self.frequenz

    def get_pin(self):
        return self.pwmpin

    def get_PulseRange(self):
        return self.PRMin, self.PRMax

    def get_operating_angle(self):
        return self.operating_angle
    
    def STOP(self):
        self.pwmpin.ChangeDutyCycle(0)
        
    def degree_to_cycle(self, degrees):
        return self.PRMin + degrees * ((self.PRMax - self.PRMin) / self.operating_angle)

    def change_frequenz(self, frequenz):
        self.pwmpin.ChangeFrequency(frequenz)

    def change_position(self, degrees):
        for localDegrees in range(0, degrees)
            self.pwmpin.ChangeDutyCycle(self.degree_to_cycle(localDegrees))
