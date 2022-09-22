# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:29:18 2020

@author: ASUS
"""

n,m=input().split()
total=0
list1=list(map(int,input().split()))
set1=set(map(int,input().split()))
set2=set(map(int,input().split()))
for i in list1:
    if i in set1:
        total=total+1
    elif i in set2:
        total=total-1
        
print(total)
        
        
