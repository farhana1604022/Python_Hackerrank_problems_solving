# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:51:35 2020

@author: ASUS
"""

a=int(input())
set1=set(map(int,input().split()))
b=int(input())
for i in range(b):
    cmd=input().split()
    if cmd[0]=="remove":
        set1.remove(int(cmd[1]))
    elif cmd[0]=="discard":
        set1.discard(int(cmd[1]))
    elif cmd[0]=="pop":
        set1.pop()
    else:
        assert False
print(sum(set1))    
    