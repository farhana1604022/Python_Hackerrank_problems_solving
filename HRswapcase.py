# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:48:27 2020

@author: ASUS
"""
'''
s=input()
s2=s.swapcase()
print(s2)
'''
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)