# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:50:07 2020

@author: ASUS
"""

a1=-1
a2=1
c=int(input("Enter the termth number"))
for i in range(1,c+1):
    f=a1+a2
    print(f"{f} ")
    a1=a2
    a2=f