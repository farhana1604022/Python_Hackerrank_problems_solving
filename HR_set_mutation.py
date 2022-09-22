# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:24:02 2020

@author: ASUS
"""

n=int(input())
set1=set(map(int,input().split()))
a=int(input())
for _ in range(a):
    x,_=input().split()
    set2=set(map(int,input().split()))
    if x =="intersection_update":
        (set1).intersection_update(set2)
    elif x   =="update":
        set1.update(set2)
    elif x =="difference_update":
       set1.difference_update(set2)
    elif x  =="symmetric_difference_update":
       set1.symmetric_difference_update(set2)
y=sum(set1)
print(y)
