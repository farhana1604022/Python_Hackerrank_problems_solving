# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:53:35 2020

@author: ASUS
"""

a=int(input("Enter numn1"))
b=int(input("Enter numn2"))
c=max(a,b)

for i in range(1,c+1):
    if(a%i==0 and b%i==0):
        d=i
        
print(d)


