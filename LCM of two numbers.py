# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 10:18:02 2020

@author: ASUS
"""

a=int(input("Enter numn1"))
b=int(input("Enter numn2"))
c=max(a,b)

while(1):
    if(c%a==0 and c%b==0):
        print(f"The LCM of {a} & {b} is {c}")
        break;
    else:
        c=c+1