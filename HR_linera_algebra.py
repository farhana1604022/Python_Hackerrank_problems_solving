# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:58:00 2020

@author: ASUS
"""
import numpy as np
n=int(input())
x=np.array([input().split() for _ in range(n)],float)

print(round(np.linalg.det(x),2))

#print(round(numpy.linalg.det(numpy.array([input().split() for _ in range(int(input()))],float)),2))
