# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:51:08 2024

@author: ACER
"""

def tong_1(n):
    s = 0
    for i in range(1,n+1):
        s = s + i
    return s

def tong_2(n):
    s = 0
    for i in range(1,n+1):
        s = s + i**2
    return s

def tong_3(n):
    s = 0 
    for i in range(1,n+1):
        s = s+ (1/i)
    return s

def tong_4(n):
    s = 0
    giai_thua = 1
    for i in range(1,n+1):
        giai_thua = giai_thua * i
        s = s + giai_thua
    return s   

def tong_5(n):
    s = 1
    for i in range(1,n+1):
        s = s*i
    return s






if __name__=="__main__":
    print(tong_1(4))
    print(tong_2(4))
    print(tong_3(4))
    print(tong_4(4))
    print(tong_5(4))