# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:29:42 2020

@author: ASUS
"""

a=int(input())
x=list(map(int,input().split()))
print(x)
b=int(input())
y=list(map(int,input().split()))
print(y)
   
print(len(set(x).union(set(y))))
