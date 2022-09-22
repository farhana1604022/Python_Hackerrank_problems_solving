# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:54:34 2020

@author: ASUS
"""
import numpy as np
a,b=map(int,input().split())
x=np.array([input().split() for _ in range(a)],int)
y=np.max(np.min(x,axis=1))
print(y)
