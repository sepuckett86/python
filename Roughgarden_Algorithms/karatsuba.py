#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:46:23 2017
Karatsuba algorithm
@author: Susan
"""

def karatsuba1(x, y):
    """
    Karatsuba multiplication reduces the number of recursive calls from 4 to 3,
    compared to grade-school calculations
    
    Still working on this

    """
    
    x = str(x)
    y = str(y)
    
    if len(x) == 1 or len(y) == 1:
        return int(x)*int(y)
    else:
        
        #divide each number into two halves
        a = int(x[0:int(len(x)/2)])
        b = int(x[int(len(x)/2):])
        c = int(y[0:int(len(y)/2)])
        d = int(y[int(len(y)/2):])
        
        #define products using karatsuba
        ac = karatsuba1(a,c)
        bd = karatsuba1(b,d)
        
        #karatsuba multiplication
        n = len(x)
        nby2 = len(x)/2
        product = (10**n)*ac+(10**(nby2))*((a+b)*(d+c)-ac-bd)+bd
        return int(product)


'''
# From https://pythonandr.com/2015/10/13/karatsuba-multiplication-algorithm-python-code/

def karatsuba(x,y):
	"""Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		nby2 = n / 2
		
		a = x / 10**(nby2)
		b = x % 10**(nby2)
		c = y / 10**(nby2)
		d = y % 10**(nby2)
		
		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
        
        	# this little trick, writing n as 2*nby2 takes care of both even and odd n
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

		return prod
 '''   
first = 1234
second = 5678
print(karatsuba1(first,second))
print(first*second)
