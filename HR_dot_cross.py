# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:47:41 2020

@author: ASUS
"""

import numpy as np
n=int(input())
a=np.array([input().split() for _ in range(n)],int)
b=np.array([input().split() for _ in range(n)],int)
print(np.dot(a,b))