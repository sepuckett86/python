#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:36:39 2017
For Coursera Genomic Data Science --Python
"(4) A repeat is a substring of a DNA sequence that occurs in multiple 
copies (more than one) somewhere in the sequence. Although repeats can 
occur on both the forward and reverse strands of the DNA sequence, we 
will only consider repeats on the forward strand here. Also we will allow
 repeats to overlap themselves. For example, the sequence ACACA contains
 two copies of the sequence ACA - once at position 1 (index 0 in Python),
 and once at position 3. Given a length n, your program should be able to
 identify all repeats of length n in all sequences in the FASTA file. Your
 program should also determine how many times each repeat occurs in the 
 file, and which is the most frequent repeat of a given length."
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
    
#Make a list of the DNA sequences
DNA_list = list(seqs.values())
identifier_list = list(seqs.keys())    

#ask for length input from user
len_repeat = input('Length of Repeat: ')
len_repeat = int(len_repeat)


#want dictionary with repeat seq: #repeats
pot_repeat_number = {}
repeat_number = {}
#loop over each seq in DNA list
for x in DNA_list:
    #iterate over entire sequence
    for i in range(0, len(x)-len_repeat+1):
        pot_repeat = x[i:i+len_repeat]
        if pot_repeat in pot_repeat_number:
            pot_repeat_number[pot_repeat] += 1
        else:
            pot_repeat_number[pot_repeat] = 1

for k,v in pot_repeat_number.items():
    if v > 1:
            repeat_number[k] = v    
                
print (repeat_number) 
repeat_list = list(repeat_number.keys()) 
number_list = list(repeat_number.values())              

#MOST FREQUENT REPEAT OF A GIVEN LENGTH

#reverse the dictionary
number_repeat = {}
for x, y in zip(repeat_list, number_list):
    number_repeat.setdefault(y,[]).append(x)
    
#determine most frequent number
if number_list != []:
    most_freq_no = max(number_list)
else: most_freq_no = 0
print ("The most freq repeat occurs %d times" %most_freq_no)

#find most freq repeats
if most_freq_no != 0:
    most_freq_repeats = number_repeat[most_freq_no]
    print ("The most frequent repeats are: " + str(most_freq_repeats))
