# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 22:06:12 2020

@author: ASUS
"""

"""
a=int(input())
set1=set(map(int,input().split()))
b=int(input())
for i in range(b):
    cmd,_=input().split()
    if cmd=="remove":
        
"""
''''
n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))
'''
a=int(input())
set1=set(map(int,input().split()))
for i in range(int(input())):
    eval('set1.{0}({1})'.format(*input().split()+['']))
print(sum(set1))