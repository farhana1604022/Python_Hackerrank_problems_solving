# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 20:08:55 2020

@author: ASUS
"""

def fibonacci_squares(n):
    s=0
    f0=0
    f1=1
    if n<=1:
        return n
    for i in range(2,n+1):
        f=f0+f1
        s=(s+(f**2))%10
        f0=f1
        f1=f
    return (s+1)

n=int(input())
print(fibonacci_squares(n))

    
    
    
    
    
    
        
        
    