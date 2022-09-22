# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 09:52:12 2020

@author: ASUS
"""

a=int(input())
lst1=list(map(int,input().split()))
b=int(input())
lst2=list(map(int,input().split()))

result=len(set(lst1).intersection(lst2))
print(result)