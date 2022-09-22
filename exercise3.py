# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:02:03 2020

@author: ASUS
"""

a=[1,2,3,4,5,6,7,8,9,10,5,22]
b=[]
x=len(a)
print(x)
for i in range(x):
    if a[i]<=5:
        b.append(i)
       