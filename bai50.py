# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:41:42 2024

@author: ACER
"""

def kiem_tra_so(n):
    if n < 0 and n % 2 != 0:
        return -1
    elif n > 0 and n% 2 ==0:
        return 1
    else:
        return 0
print(kiem_tra_so(7))