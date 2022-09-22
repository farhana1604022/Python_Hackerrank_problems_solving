# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:13:51 2020

@author: ASUS
"""
import cmath
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=(b**2)-4*a*c
x1=(-b+cmath.sqrt(d))/(2*a)
x2=(-b-cmath.sqrt(d))/(2*a)

print("1st root is :%.2f and 2nd root is: %.2f " %x1 %x2)
