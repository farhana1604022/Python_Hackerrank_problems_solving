# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:46:29 2020

@author: ASUS
"""
import math
opposite=int(input())
adjacent=int(input())
x=(opposite)/(adjacent)
print(f"{round(math.atan(x)*(180/3.1416))}°")
