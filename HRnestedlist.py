# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:37:57 2020

@author: ASUS
"""

if __name__ == '__main__':
    lst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ele=[name,score]
        lst.append(ele)
    lst.sort()   
    print(lst)
    #for i in lst:  
       # for i in lst