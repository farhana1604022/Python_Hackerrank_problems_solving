# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:57:33 2020

@author: ASUS
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a,b=list(map(str,input().split()))
x=permutations(a.sort(),int(b))
for i in x:
    print(i)
