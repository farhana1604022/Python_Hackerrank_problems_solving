# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:05:13 2020

@author: ASUS
"""

a=int(input("enter a num1: "))
b=int(input("enter num2 :"))
for i in range(a,b):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
            
            
        