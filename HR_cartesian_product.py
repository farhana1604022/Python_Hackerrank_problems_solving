# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:55:56 2020

@author: ASUS
"""

from itertools import product 
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=list(product(a,b))
for i in  x:
    print(i,end=" ")
