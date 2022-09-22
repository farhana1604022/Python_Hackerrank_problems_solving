# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:02:33 2020

@author: ASUS
"""

a=int(input())
list1=list(map(int,input().split()))
b=int(input())
list2=list(map(int,input().split()))
print(len(set(list1).difference(set(list2))))