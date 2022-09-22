# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 12:34:04 2020

@author: ASUS
"""


def fibonacci(n):
    f0=0
    f1=1
    if n<0:
        print("Error")
    elif (n<=1):
        return n
    else:
        for i in range(2,n+1):
            f=(f0+f1)%10
            f0=f1
            f1=f
            
    return f

a=int(input())
print(fibonacci(a))     