# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:59:49 2020

@author: ASUS
"""
"""
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))
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
            f=f0+f1
            f0=f1
            f1=f
            
    return (f)

a=int(input())
print(fibonacci(a))        
                
            
        
    
    