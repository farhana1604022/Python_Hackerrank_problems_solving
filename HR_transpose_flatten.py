# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:20:54 2020

@author: ASUS
"""
import numpy as np
n,m=map(int,input().split())
x=np.array([input().split() for _ in range(n)],int)
print(np.transpose(x))
print(x.flatten())
