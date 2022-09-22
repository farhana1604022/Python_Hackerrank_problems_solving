# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 10:35:59 2020

@author: ASUS
"""

s1=input()
i,c=input().split()
lst=list(s1)
print(lst)
lst[int(i)]=c
s1=''.join(lst)
print(s1)
