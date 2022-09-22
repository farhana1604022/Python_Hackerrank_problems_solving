# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:33:59 2020

@author: ASUS
"""
# here balslash \ is a line continution character
def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current  \
        = current, (previous + current) % m 
          
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1
#print(pisanoPeriod(2))

def fibonacci(n,m):
    pisano_period=pisanoPeriod(m)
    n=n%pisano_period
    f0=0
    f1=1
    if n<0:
        return "error"
    elif n<=1:
        return 1
    for i in range (2,n+1):
        f=(f0+f1)%m
        f0=f1
        f1=f
    return f
n,m=map(int,input().split())
       
print(fibonacci(n,m)) 
#print(fibonacci(2816213588,239))     
    
    



