# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 00:15:42 2020

@author: ASUS
"""
f1=open("input1.txt",'w')
items=f1.write('[5, 7, 10, 12, 15]')
f1.close()
#items = [5, 7, 10, 12, 15]

print("list of items is", items)

x = int(input("enter item to search:"))
 
i = flag = 0
 
while i < len(items):
	if items[i] == x:
		flag = 1
		break
 
	i = i + 1
 
if flag == 1:
	print("item found at position:", i + 1)
else:
	print("item not found")
