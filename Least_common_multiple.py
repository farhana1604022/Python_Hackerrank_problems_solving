# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:06:09 2020

@author: ASUS
"""

def gcd(a,b):
    r=a%b
    while r!=0:
        a=b
        b=r
        r=a%b
    return b

def lcm(a,b):
    result=int((a*b)/gcd(a,b))
    return result
a,b=map(int,input().split())
print(lcm(a,b))

