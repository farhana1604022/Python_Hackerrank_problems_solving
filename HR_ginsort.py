# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:35:33 2020

@author: ASUS
"""

x=list(input())
y=sorted(*x,reverse=True)
for i in y:
    print(i,end="")