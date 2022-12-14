# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:59:59 2020

@author: ASUS
"""

#!/bin/python3

import math
import os
import random
import re
import sys


class Car:
    
    def __init__(self,maxspeed,unit):
        self.maxspeed=maxspeed
        self.unit=unit
        
    def __str__(self):
        return "Car with the maximum speed of {} {}".format(self.maxspeed,self.unit)
    
    pass

class Boat:
    def __init__(self,maxspeed2):
        self.maxspeed2=maxspeed2
        
    def __str__(self):
        return "Boat with the maximum speed of {} knots".format(self.maxspeed2)
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()
