# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:16:50 2020

@author: ASUS
"""

#quadratic equation solving
import cmath
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c :"))
des=(b**2)-(4*a*c)

sol1=(-b+cmath.sqrt(des))/(2*a)
sol2=(-b-cmath.sqrt(des))/(2*a)

print("the solations are {0} and {1}" .format(sol1,sol2))