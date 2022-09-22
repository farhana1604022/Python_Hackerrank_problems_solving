# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:59:18 2020

@author: ASUS
"""
n=int(input())
list1=[]
for i in range(n):
    x=input()
    y=float(input())
    list1.append([x,y])
set1=sorted(set(x[1] for x in list1))
#set used because it will have only unique elements so index 1 ey 2nd lowest grade peeye jabo
"""
for name in sorted(x[0] for x in list1 if x[1]==set1[1]):
    print(name)
print(set1)
"""
print('\n'.join([a for a,b in sorted(list1) if b==set1[1]]))