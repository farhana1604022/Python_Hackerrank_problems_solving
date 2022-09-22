# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:31:10 2020

@author: ASUS
"""


print("Enter 1 for add operation:")

print("Enter 2 for subtraction operation:")

print("Enter 3 for multiplication operation:")

print("Enter 4 for divide operation:")

n=int(input("Enter a operation: 1/2/3/4: "))
a=int(input("enter number1 :"))
b=int(input("enter number2 :"))
if(n==1):
    print(f"The result is :{a+b}")
elif(n==2):
     print(f"The result is :{a-b}")
elif(n==3):
     print(f"The result is :{a*b}")    
    
else:
    print(f"The result is {a/b}")
    