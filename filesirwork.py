# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:52:21 2020

@author: ASUS
"""

file=open("user2.txt","w")

items = ["5", "7", "10", "12", "15"]
with file as f:
    for i in range(0,len(items)):
        f.write(items[i]+"\n")


def main():
    x=int(input("Enter a item to search : "))
    i=flag=0
    while i<len(items):
        if int(items[i])==x:
            flag=1
            break
        i=i+1
    if flag==1:
        print("The item is at position :",i+1)
    else:
        print("Ithem not found")
 
main()    
'''
def main2():
    file1=open("user2.txt","r")
    
    for line in file1:
'''    