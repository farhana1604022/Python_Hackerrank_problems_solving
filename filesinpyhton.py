# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:32:56 2020

@author: ASUS
"""

myFile=open('myfile.txt','w')
print('Name :',myFile.name)
myFile.write("I love my country\n")
myFile.write("i love python and c++\n")
myFile.close()
myFile=open('myfile.txt','r')
text=myFile.read()
print(text)

