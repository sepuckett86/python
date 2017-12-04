#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 13:51:18 2017
Integer multiplication without the * character
@author: Susan
"""
import time

#show elapsed time it takes to complete a function
def show_time(function, arg, arg2):
    start = time.time()
    out = function(arg, arg2)
    end = time.time()
    print("\tTime elapsed: %f" %(end - start) + " sec")
    return(end - start, out)
    
# Make mult table
mult_table = [] 
for i in range(10):
    for j in range(10):
        add_table = {0: 0,
                     1: j,
                     2: j+j,
                     3: j+j+j,
                     4: j+j+j+j,
                     5: j+j+j+j+j,
                     6: j+j+j+j+j+j,
                     7: j+j+j+j+j+j+j,
                     8: j+j+j+j+j+j+j+j,
                     9: j+j+j+j+j+j+j+j+j
             }   
        k = add_table[i]
        row = [i, j, k]
        mult_table.append(row)

# Function for multiplication of integers under 10
def multiply_low(x, y):
    if int(x) > 9 or int(y) > 9:
            return print("number too big")
    for item in mult_table:
        if item[0] == x and item[1] == y:
            return int(item[2])
            
# Function for multiplication of any two integers
# Old-school method
def multiply(x, y):
    # Make x the biggest number
    if y > x:
        store = x
        x = y
        y = store
    x = str(x)
    y = str(y)
    final_ans = 0
    move_over = ""
    for j in range(len(y)):
        digit_y = int(y[-1-j])
        ans = move_over
        carry = 0
        for i in range(len(x)):
            digit_x = int(x[-1-i])
            mult_dig_xy = str(carry + multiply_low(digit_x, digit_y))
            # for two digits, carry the first, keep the second
            if len(mult_dig_xy) == 2:
                carry = mult_dig_xy[0]
                ans = mult_dig_xy[1] + ans
                if i == len(x)-1:
                    ans = str(carry) + ans
            # for one digit, keep the digit
            elif len(mult_dig_xy) == 1:
                ans = mult_dig_xy[0] + ans
                carry = 0       
            carry = int(carry)
        move_over = move_over + "0"
        final_ans += int(ans)
    return final_ans

# Function that is methodical but easy to write
def mult_easy(x, y):
    total = 0
    if y > x:
        store = x
        x = y
        y = store
    for i in range(y):
        total += x
    return total

# Function that is Python's standard multiplication using * character
def mult_cheat(x, y):
    return x*y
            
# Enter integers to multiply
number1 = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))
print("\b")
print("Old-school method")
c, b = show_time(multiply, number1, number2)
a = (number1*number2)
print("\tAnswer: {0}".format(b))

print("\b")
print("Using built-in * calculator")
built_a, built_b = show_time(mult_cheat, number1, number2)
print("\tAnswer: {0}".format(built_b))