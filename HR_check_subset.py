# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:16:27 2020

@author: ASUS
"""

T=int(input())
for i in range(T):
    a=int(input())
    list1=list(map(int,input().split()))
    b=int(input())
    list2=list(map(int,input().split()))
    print(set(list1).issubset(set(list2)))
    
    """for i in list1:
        if i not in list2:
            print("False")
            break
    
        print("True")
        
   """         
            
    
    