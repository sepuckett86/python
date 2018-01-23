#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 18:32:41 2018
Skew diagram for E. coli
@author: Susan
"""

import scipy as sp
import matplotlib.pyplot as plt

def skew(Genome):
    '''
    Exercise Break: Give all values of Skewi (GAGCCACCGCGATA) for i ranging from 0 to 14.

    Sample Input:
     CATGGGCATCGGCCATACGCC

    Sample Output:
     0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2
     
     C: -1
     G: +1
     A,T: no change

    '''
    skew_out = '0'
    n = 0
    for i in range(1,Genome.size+1):
        if Genome[i-1] == 'C':
            n -= 1
        if Genome[i-1] == 'G':
            n += 1
        skew_out = skew_out + ' ' + str(n)
    return skew_out


# Open E. coli genome
    
with open('mtb.txt') as f:
    test = ''
    for line in f:
        test = test + line
  
# Make into array to speed it up    
test = list(test)
test = sp.array(test)
test_shift = sp.zeros(test.size)
test_shift[test == 'G'] = 1
test_shift[test == 'C'] = -1
test_shift[test == 'A'] = 0
test_shift[test == 'T'] = 0
y = sp.cumsum(test_shift)

plt.plot(y)

"""
y = sp.array(skew(test).split(), dtype = int)

ntest = y.size

yplot = y[0::ntest//100]
print(yplot.size)

plt.plot(yplot)
"""
'''
x = sp.linspace(0.1,4,50)
y0 = x ** 2
y1 = x ** (0.5)
y2 = x

print(x, y0, y1)

plt.plot(x,y0)
plt.plot(x,y1)
plt.plot(x,y2)
'''