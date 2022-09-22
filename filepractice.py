# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:05:23 2020

@author: ASUS
"""
"""
fileref=open("sample.txt","r")
contents=fileref.read()
print(contents)
print(contents[:100])
fileref.close()
"""
"""
fileref=open("sample.txt","r")
contents=fileref.readlines()
for line in contents:
    print(line.strip())
    print(len(line))
 """
#print(contents)
fileref=open("sample.txt","r")

for line in fileref:
    print(line.strip())
fileref.close()