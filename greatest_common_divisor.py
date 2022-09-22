# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:58:30 2020

@author: ASUS
"""

def gcd(a,b):
    r=a%b
    while r!=0:
        a=b
        b=r
        r=a%b
        
    return b
 
a,b=map(int,input().split())

print(gcd(a,b))