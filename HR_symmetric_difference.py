# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:33:15 2020

@author: ASUS
"""

a=int(input())
list1=list(map(int,input().split()))
b=int(input())
list2=list(map(int,input().split()))
result=set(list1).symmetric_difference(list2)
x=list(result)
y=sorted(x)#as sort fucntion doesnot return any value ,so i used sorted fucntion as it returns a iterable list
print(y)
for i in y:
    print(i)
    
