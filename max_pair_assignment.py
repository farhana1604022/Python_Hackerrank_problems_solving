# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 13:09:14 2020

@author: ASUS
"""

length=int(input())
list1=list(map(int, input().split()))
#print(list1)
list_sorted=sorted(list1,reverse=True)
#print(list_sorted)
print(list_sorted[0]*list_sorted[1])