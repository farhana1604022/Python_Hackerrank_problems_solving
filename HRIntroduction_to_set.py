# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:49:19 2020

@author: ASUS
"""

def average(array):
    #et(array)
    x=set(array)
    y=len(x)
   # return x
    return (sum(x)/y)

    
if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    
    result=average(arr)
    print(result)
    
    
"""
st=(input() for i in range(int(input())))
print(st)
"""