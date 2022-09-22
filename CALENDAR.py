# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:23:25 2020

@author: ASUS
"""

import calendar
#yy=2020
#mm=11

mm=int(input())
dd=int(input())
yyyy=int(input())
#display the calendar
print(calendar.month(yyyy,mm))
print(calendar.day(mm,dd,yyyy))