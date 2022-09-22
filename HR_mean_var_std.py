# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:18:45 2020

@author: ASUS
"""

import numpy as np
np.set_printoptions(legacy='1.13')
n,m=map(int,input().split())
array1=np.array([input().split() for _ in range(n)],int)
print(np.mean(array1,axis=1))
print(np.var(array1,axis=0))
print(np.std(array1))