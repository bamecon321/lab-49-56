# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:56:51 2024

@author: ACER
"""
import math
def canbac(x,n):
    return x**(1/n)

def sodao(n):
    #str chuoi, chu so 
    return int(str(n)[::-1])

#Cach 3 tinh toan
def dao(n):
    dao = 0
    while n > 0:
        dao = dao * 10 + n%10
        n//=10
    return dao

def chinhphuong(n):
    return int(math.sqrt(n)) ** 2 == n

def kiemtrasonguyento(n):
    if n < 2:
     return False
    for i in range(2,n):
     if n%i == 0:
       return False
    return True

def tichcacchusole(n):
    s = 1
    for i in str(n):
      if int(i)%2 !=0:
        s = s * int(i)
    return s

def tongcacnguyentonhohonn(n):
    s = 0
    for i in range(2,n):
        if kiemtrasonguyento(i):
            s = s+i
    return s
    
def tongcacsochinhphuongnhohonn(n):
    s = 0
    for i in range(1,n):
        if chinhphuong(i):
            s = s + i
    return s                   

def tongcacuocsoduongn(n):
    s = 0
    for i in range(1,n+1):
        if n%i == 0:
            s = s+i
    return s
    













if __name__ =="__main__":
    print(canbac(8,3))
    print(sodao(123450))
    print(dao(123450))
    print(chinhphuong(17))
    print(kiemtrasonguyento(2))
    print(tichcacchusole(195))
    print(tongcacnguyentonhohonn(20))
    print(tongcacsochinhphuongnhohonn(9))
    print(tongcacuocsoduongn(16))
    