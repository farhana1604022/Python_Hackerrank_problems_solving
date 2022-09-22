# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:16:32 2020

@author: ASUS
"""

from collections import Counter

list=[1,1,2,2,3,4,4,4,5,8,1]
cnt=Counter(list)
print(cnt)

de={1:1,4:2}
cnt.subtract(de)
print(cnt)
