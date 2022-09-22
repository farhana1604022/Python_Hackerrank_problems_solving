# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:41:18 2020

@author: ASUS
"""


x=int(input())
y=int(input())
z=int(input())
n=int(input())
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range (z+1) if ((i+j+k)!=n)])