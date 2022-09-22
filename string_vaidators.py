# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:39:22 2020

@author: ASUS
"""

s=input()
print(any(character.isalnum() for character in s))        
print(any(character.isalpha() for character in s))
print(any(character.isdigit() for character in s))
print(any(character.islower() for character in s))
print(any(character.isupper() for character in s))