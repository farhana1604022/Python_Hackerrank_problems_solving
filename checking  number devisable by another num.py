# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:59:47 2020

@author: ASUS
"""
'''
list1=[13,65,39,22,44,56,83,33]
list2=list(filter(lambda x: x%13==0,list1))
print(list2)

'''
a=int(input("Enter a number to check : "))
list1=[]
b=int(input("Enter the length of the list : "))
for i in range (b):
    data=int(input())
    list1.append(data)
print(list1)