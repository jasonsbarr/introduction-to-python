#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:22:34 2020

@author: jason
"""
# 2.2: Conditionals
x = int(input("Give me a number (1 of 3): "))
y = int(input("Give me a number (2 of 3): "))
z = int(input("Give me a number (3 of 3): "))

if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print("None of them are odd")
else:
    if not x % 2 == 0:
        if y % 2 == 0 and z % 2 == 0:
            print(x)
        elif not y % 2 == 0 and x > y:
            if z % 2 == 0 or not x % 2 == 0 and x > z:
                print(x)
            else:
                print(z)
        elif not y % 2 == 0 and y > x:
            if z % 2 == 0 or not z % 2 == 0 and y > z:
                print(y)
            else:
                print(z)
    elif not y % 2 == 0:
        if x % 2 == 0 and z % 2 == 0:
            print(y)
        elif x % 2 == 0 or not x % 2 == 0 and y > x:
            if z % 2 == 0 or not z % 2 == 0 and y > z:
                print(y)
            else:
                print(z)
        elif z % 2 == 0 or not z % 2 == 0 and y > z:
            if x % 2 == 0 or not x % 2 == 0 and y > x:
                print(y)
            else:
                print(x)
    elif not z % 2 == 0:
        if x % 2 == 0 and y % 2 == 0:
            print(z)
        elif x % 2 == 0 or not x % 2 == 0 and z > x:
            if y % 2 == 0 or not y % 2 == 0 and z > y:
                print(z)
            else:
                print(y)
        elif y % 2 == 0 or not y % 2 == 0 and z > y:
            if x % 2 == 0 or not x % 2 == 0 and z > x:
                print(z)
            else:
                print(x)

# 2.4: Iteration
largest = -10000
i = 0
while i < 10:
    n = int(input("Enter an integer: "))
    if not n % 2 == 0 and n > largest:
        largest = n
    i += 1

if largest == -10000:
    print("No odd numbers given")
else:
    print(largest)
