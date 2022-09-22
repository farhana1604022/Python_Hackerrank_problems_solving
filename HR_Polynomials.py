# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:47:29 2020

@author: ASUS
"""

import  numpy as np
a=np.array(list(map(float,input().split())))
x=int(input())
print(np.polyval(a,x))