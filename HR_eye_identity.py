# Enter your code here. Read input from STDIN. Print output to STDOUT
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:19:24 2020

@author: ASUS
"""

import numpy as np
n,m=map(int,input().split())
#print(numpy.identity(3))
print(np.eye(n, m))
