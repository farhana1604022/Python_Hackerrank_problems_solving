# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:44:02 2020

@author: ASUS
"""
import numpy
x,y,z=list(map(int,input().split()))
n=x+y
for i in range(n):
    x=numpy.array(list(map(int,input().split())))
    y=numpy.concatenate((x),axis=0)
print(y)    

#print(n)