# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:57:14 2020

@author: ASUS
"""

x=int(input())
flag="Flase"
list1=list(map(int,input().split()))
if all(list1>0):
    if any(list1==str(list1).reverse()):
        flag="True"

print(flag)