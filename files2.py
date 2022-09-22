# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:46:27 2020

@author: ASUS
"""

f=open("pyfille.txt","w+")

for i in range(10):
    f.write(f"This is line {i+1}\n")
f.close()    