#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:57:06 2017
Powers of 2
@author: Susan
"""
import math

x = int(input("what is n? "))

y1 = 2**x
y2 = x**2

y3 = 2**y1
y4 = 2**y2
y5 = x**y1

y6 = math.log(x, 2)
y7 = (x**2)*y6


print("2^(2^n) = {}".format(y3))
print("2^(n^2) = {}".format(y4))
print("n^2 * log(n) = {}".format(y7))
print(x)
print("n^(2^n) = {}".format(y5))