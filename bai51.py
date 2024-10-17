# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:53:04 2024

@author: ACER
"""

def kiem_tra():
    n = int(input("Nhap vao so n: "))
    if -89 <= n <= 90:
        return n
    print("Khong hop le")
    return kiem_tra()
print(kiem_tra())