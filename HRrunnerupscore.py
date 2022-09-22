# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:06:20 2020

@author: ASUS
"""
'''
n=int(input())
list1=[]
list2=[]
for i in range(n):
    data=int(input())
    list1.append(data)
print(list1)



  
# Sorting list of Integers in descending 
list1.sort(reverse = True) 
  
print(list1)
max=list1[0]
for j in range(n):
    if(list1[j]<max):
        print(list1[j])
        break
    
  '''
n = int(input())
arr = list(map(int, input().split()))[:n]     
print(n)
print(arr)
arr.sort(reverse=True)
print(arr)
max=arr[0]
for i in range(n):
    if arr[i]<max:
        print(arr[i])
        break