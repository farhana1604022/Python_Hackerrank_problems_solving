# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:26:10 2020

@author: ASUS
"""

import numpy as np 
a=np.array(list(map(int,input().split())))
b=np.array(list(map(int,input().split())))
print(np.inner(a,b))
print(np.outer(a,b))