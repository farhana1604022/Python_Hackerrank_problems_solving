# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:14:18 2020

@author: ASUS
"""
import numpy as np
x=list(map(int,input().split()))
y=np.array(x)

print(np.reshape(y,(3,3)))
