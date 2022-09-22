# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:29:42 2020

@author: ASUS
"""

import numpy as np
n,m=map(int,input().split())
array_a=np.array([input().split() for _ in range(n)],int)
array_b=np.array([input().split() for _ in range(n)],int)
print(np.add(array_a,array_b))
print(np.subtract(array_a,array_b))
print(np.multiply(array_a,array_b))
print(np.divide(array_a,array_b))
print(np.mod(array_a,array_b))
print(np.power(array_a,array_b))