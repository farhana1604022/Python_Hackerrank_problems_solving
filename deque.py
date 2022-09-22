# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:02:22 2020

@author: ASUS
"""
from collections import deque
list=['a','b','a']
var=deque(list)
print(var.count('a'))
var.append('e')
print(var)
var.appendleft('s')
print(var)
var.pop()
print(var)
var.popleft()
print(var)