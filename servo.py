#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""servo.py:	Servo class"""

__author__ = "Raphael Kreft & Marc Steinebrunner"
__copyright__ = ""
__version__ = "Development v0.02"
__email__ = "raphaelkreft@gmx.de & marc.steinebrunner@gmail.com"
__status__ = "Dev"

import RPi.GPIO as gpio


class Servo(object):
    def __init__(self, pin, frequenz, PulseRangeMinInUS, PulseRangeMaxInUS, operating_angle):
        gpio.setmode(gpio.BOARD)
        gpio.setup(pin, gpio.OUT)
        gpio.setwarnings(False)

        self.frequenz = frequenz
        self.pwmpin = gpio.PWM(pin, frequenz)
        self.PRMin = PulseRangeMinInUS / 1000
        self.PRMax = PulseRangeMaxInUS
        self.operating_angle = operating_angle

    def get_frequenz(self):
        return self.frequenz

    def get_pin(self):
        return self.pwmpin

    def get_PulseRange(self):
        return self.PRMin, self.PRMax

    def get_operating_angle(self):
        return self.operating_angle

    @staticmethod
    def degree_to_cycle(self, degrees):
        if (self.operating_angle == 180):
            return self.PRMin + degrees * ((self.PRMax - self.PRMin) / 180)
        elif (self.operating_angle == 360):
            return self.PRMin + degrees * ((self.PRMax - self.PRMin) / 360)

    def change_frequenz(self, frequenz):
        self.pwmpin.ChangeFrequency(frequenz)

    def change_position(self, degrees):
        self.pwmpin.ChangeDutyCycle(self.degree_to_cycle(degrees))
