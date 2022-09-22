# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 10:32:43 2020

@author: ASUS
"""
#simple for loop
people=['jhon','paul','sara','susan']

for person in people:
    print(f" name is {person} ")
for person in people:
    if person=='sara':
        break
    
 
    print(f"current people is  :{person}")


number=[1,2,3,4,5,6,7,8,9,6]
for i in number:
     print(i)
for i in number:
    print(i)
#continue
for i in number:
    if i==7:
        continue
    print(i)
for i in number:
    if i==7:
        break
    print(i)

for i in range(len(number)):
    print(i+1)

for i in range(0,11):
    print(i)
    
    
    