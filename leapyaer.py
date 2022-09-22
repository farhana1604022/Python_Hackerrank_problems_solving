# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:29:01 2020

@author: ASUS
"""

year=int(input("Enter a year"))
if(year%4 ==0 and year%100!=0 or year%400==0):
    print(f"The year {year} is leap year")
else:
    print(f"{year} is not  a leap year")