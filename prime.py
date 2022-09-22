# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:11:07 2020

@author: ASUS
"""

a=int(input("enter a number"))

for i in range(2,a):
    if(a%i==0):
        print(f"{a} is not a prime number")
        break
        #print(f"{i} times {b} is {a}" )
else:
   print(f"{a} is  a prime number")