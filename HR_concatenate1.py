# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:04:27 2020

@author: ASUS
"""


import numpy as np
n,m,p=map(int,input().split())
x=np.array([input().split() for _ in range(n)],int)
y=np.array([input().split() for _ in range(m)],int)
print(np.concatenate((x,y)))