# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:42:59 2020

@author: ASUS
"""
lst=[]
for i in range(int(input())):
     cmd=input().split()
     for i in range(1,len(cmd)):
         cmd[i]=int(cmd[i]) 
     if cmd[0]=="insert":
         lst.insert(cmd[1],cmd[2])
     elif cmd[0]=="append":
         lst.append(cmd[1])
         
     elif cmd[0]=="remove":
         lst.remove(cmd[1])
     elif cmd[0]=="pop":
         lst.pop()
     elif cmd[0]=="sort":
         lst.sort()
     elif cmd[0]=="reverse":
         lst.reverse()
     elif cmd[0]=="print":
         print(lst)
     
         
    
     
     
     
     
