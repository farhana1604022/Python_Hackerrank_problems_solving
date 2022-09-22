# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:49:37 2020

@author: ASUS
"""

s=set()
n=int(input())
for i in range(n):
    s.add(input())
    
set1=set(s)
ans=len(set1)
print(ans)