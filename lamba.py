# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 00:29:51 2020

@author: ASUS
"""
n=int(input("Enter a term "))
result=list(map(lambda x: 2**x,range(n+1)))

for i in range(n+1):
    print(f"2 power {i} = {result[i]}")