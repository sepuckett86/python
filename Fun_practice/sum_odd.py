#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:53:28 2017
Sum of odd numbers problem
Input: row number
Output: sum of numbers in the row

You have a pyramid of odd numbers.
Each row you gain an extra number.
It looks like this:
1
3 5
7 9 11
13 15 17 19
etc.

@author: Susan
"""    
        
# Define odd number
def odd(index):
    return 1 + 2 * index

# How many numbers came before this row
def numbers_before(row):
    x = row
    total = 0
    while x > 0:
        x -= 1
        total = total + x
    return total

# Slow method that works 
def sum_odd(row):
    start_index = numbers_before(row)
    stop_index = start_index + row
    total = 0
    for i in range(start_index, stop_index):
        total = total + odd(i)
    return total

# Fast method that relies on patterns
def sum_odd_fast(row):
    return row ** 3
  