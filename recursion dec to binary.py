# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:16:19 2020

@author: ASUS
"""

def converttobinary(n):
    if(n>1):
        converttobinary(n/2)
    print(n%2,end='')

x=34
converttobinary(x)
print()