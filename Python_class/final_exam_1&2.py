#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:42:36 2017
For Coursera Genomic Data Science Course -- Python
"(1) How many records are in the file? A record in a FASTA file is defined as 
a single-line header, followed by lines of sequence data. The header line is 
distinguished from the sequence data by a greater-than (">") symbol in the 
first column. The word following the ">" symbol is the identifier of the 
sequence, and the rest of the line is an optional description of the entry. 
There should be no space between the ">" and the first letter of the identifier.

(2) What are the lengths of the sequences in the file? What is the longest 
sequence and what is the shortest sequence? Is there more than one longest 
or shortest sequence? What are their identifiers?"

@author: Susan
"""

#Open file
f = open('dna.example.fasta', 'r')

#Build a dictionary from reads from a fasta file for names and seqs
seqs = {}
for line in f:
  line = line.rstrip()
  if line[0] == '>':
    words = line.split()
    name = words[0][1:]
    seqs[name]=''
  else:
    seqs[name] = seqs[name] + line
    
    
    
#QUESTION 1    
#How many records are in the file?
records = len(seqs)
print ("There are %d records in the file" % records)
    


#QUESTION 2
#Determine shortest and longest DNA sequences

#Make a list of the DNA sequences
DNA_list = list(seqs.values())
names_list = list(seqs.keys())


#Make list of DNA seq lengths
len_list = []
for x in DNA_list:
    len_list.append(len(x))
    
#Make a dictionary of names/lengths
names_len = dict(zip(names_list, len_list)) 

#Sort list of lengths
sorted_len_list = sorted(len_list)

#Find how many shortest and longest sequences)
shortest = sorted_len_list[0]
longest = sorted_len_list[-1]
number_short = 0
number_long = 0

for x in len_list:
    if x == shortest:
        number_short += 1
    if x == longest:
        number_long += 1

print('The shortest sequence is %d base pairs and there are %d sequences with this length' 
      % (shortest, number_short))
print('The longest sequence is %d base pairs and there are %d sequences with this length' 
      % (longest, number_long))

#Find names of shortest and longest sequences
short_names = []
indices = [i for i,val in enumerate(len_list) if val==shortest]
for x in indices:
    short_names.append(names_list[x])    
        
long_names = []
indices = [i for i,val in enumerate(len_list) if val==longest]
for x in indices:
    long_names.append(names_list[x])      
        
print('The names of the shortest sequences are: ')
print(short_names)

print('The names of the longest sequences are: ')
print(long_names)
