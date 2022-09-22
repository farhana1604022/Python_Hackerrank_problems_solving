# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:19:09 2020

@author: ASUS
"""
import datetime
name=input("Enter your name :")
age=int(input("enter your age: "))
x=100-age
z=datetime.datetime.now()
y=x+z.year
print(f"{name} you will be 100 by {y}")
#ripaprint(f"{name} The expected year is {y}")