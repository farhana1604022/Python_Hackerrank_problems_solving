# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:52:32 2020

@author: ASUS
"""
list1=[]
list2=[]
a=int(input("Enter the length of the list: "))
for i in range(a):
    data=int(input())
    list1.append(data)
print(list1)   
b=int(input("Enter a number  to divide :")) 
for i in range(len(list1)):
    
    if(list1[i]%b==0):
        list2.append(list1[i])
        
print(list2)
