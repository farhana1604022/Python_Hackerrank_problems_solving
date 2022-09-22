# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:50:37 2020

@author: ASUS
"""

def fibonacci(n):
    f0,f1=0,1
    s=0
    if n<0:
        return "errror"
    elif n<=1:
        return n
    for i in range(2,n+1):
        f=f0+f1
        s=(s+(f**2))%10
        f0=f1
        f1=f
        
    return (s+1)
n=int(input())
print(fibonacci(n))
