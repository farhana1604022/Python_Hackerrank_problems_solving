# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:02:59 2020

@author: ASUS
"""

n=int(input())
w=len("{0:b}".format(n))
for i in range(1,n+1):
  
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b} ".format(i,width=w))