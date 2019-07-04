# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 08:21:06 2019

@author: Lenovo
"""

def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input('enter the elemnt:'))
print(n,'th fibonacci number is:',fib(n))

def fib_series(n):
    i=0
    for i in range(0,n):
        print(fib(i))
    
n=int(input('enter the elemnt:'))
print(fib_series(n))
        
    