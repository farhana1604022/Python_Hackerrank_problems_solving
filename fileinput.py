# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:36:26 2020

@author: ASUS
"""

file=open("user1.txt","w")

name=['ripa','zarif','zahid','jahanara','kalam']

with file as f:
    for i in range(0,len(name)):
        f.write(name[i]+"\n")

def main():
    inputfile=open("user1.txt","r")
    
    data=inputfile.read()
    
    print("The data of file is : \n")
    print(data)
    
    inputfile.close()
main()    