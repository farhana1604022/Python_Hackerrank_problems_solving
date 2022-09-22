# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:00:48 2020

@author: ASUS
"""

myfile=open("FILE1.txt","w")
myfile.write("My name is  Farhana Akter Ripa\n")
myfile.write("i am student of CUET\n")

myfile.close()

myfile=open("FILE1.txt","a")

for i in range(1,11):
    myfile.write(f"{i}\n")
    
myfile.close()    
