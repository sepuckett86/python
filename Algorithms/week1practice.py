#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:08:18 2017
Algorithms Week 1 practice
@author: Susan
"""

a = [1,2,3,4,5,6,6,7,7,7,4,4,4,4,4,4]

# Make a plot of list a with x values a range of length a
import matplotlib.pyplot as plt
plt.bar(range(len(a)), a)

dna = 'atgcatggtgctgca'
import collections
count = collections.Counter()
count.update(a)
print (count)
b = max(count, key=count.get)
print(b)