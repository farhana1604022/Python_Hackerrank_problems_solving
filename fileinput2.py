# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:44:54 2020

@author: ASUS
"""

def main():
    inputfile=open("user1.txt","r")
    
    data=inputfile.read()
    
    print("The data of file is : \n")
    print(data)
    
    inputfile.close()
main()    