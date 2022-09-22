# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:27:08 2020

@author: ASUS
"""

import textwrap
s=input()
max_width=int(input())
lst=textwrap.fill(s,width=max_width)
print(lst)
"""
for i in lst:
    print(i)
"""