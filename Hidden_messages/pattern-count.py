#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:52:49 2017
1.2 Hidden messages in the Replication Origin
Week One
Coursera class
@author: Susan
"""

def PatternCount(text, pattern):
    count = 0
    for i in range (0, len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

x = 'GAACTTGCGACTTGCGTCATCACTTGCGACGATGACTTGCGAAACTTGCGCTTACTTGCGCTCTTTAGAACTTGCGACTTGCGCTACTTGCGCTCAACTTGCGACTTGCGTTACTTGCGACTTGCGACTTGCGGCTGTAACTTGCGAACTTGCGACTTGCGGACTTGCGACTTGCGAGACTTGCGCTTTACTTGCGGCAGGACTTGCGCCGGTCAACTTGCGACTCCACTTGCGGGCTACTTGCGTCACTTGCGAGTGGTTACTTGCGCAATGTAACTTGCGTCACTTGCGAACGCACTTGCGAGTGTCAGCGTGGAAACTTGCGAACTTGCGGGACTTGCGCATTACTTGCGGACTTGCGACTTGCGACTTGCGTAGAGTCCCGTAAACTTGCGGCCCCAGACTTGCGTACTTGCGAACAGACTTGCGCTAAGCACTTGCGAAAACTTGCGGCACTTGCGCACTTGCGTACTTGCGTAACCCAAAAAAAGCACTTGCGATGGTACTTGCGTCCGACACTTGCGCTCAACTTGCGAGACTTGCGACTTGCGAATTACTTGCGGACTTGCGACTTGCGCCCAGACTTGCGACTTGCGCGACGCTAACTTGCGCATACTTGCGAACTTGCGTCACTTGCGACTTGCGACTTGCGGAACGTCAGACTTGCGGACTTGCGCTACTTGCGATCACTGTAACTTGCGGAACTTGCGGACTTGCGCGTACTTGCGACTTGCGTATCACTTGCGACTTGCGAGCCACTTGCGGGGGACTTGCGACTTGCGCATAAAGTCACTTGCGGACTTGCGCGGACTTGCGACTTGCGCTGGATACTTGCGAGGACTTGCGAACTTGCGGTCACTTGCGATCACAACTTGCGCACTTGCGTCACTTGCGTTACTTGCGCACGCAAGCGTAACAGTACTTGCGTGTGTTTACTTGCGAACTTGCGAACTTGCGAATACACTTGCGAC'
y = 'ACTTGCGAC'
z = 'GAACTTGCGACTTGCGTCATCACTTGCGACGATGACTTGCGAAACTTGCGCTTACTTGCGCTCTTTAGAACTTGCGACTTGCGCTACTTGCGCTCAACTTGCGACTTGCGTTACTTGCGACTTGCGACTTGCGGCTGTAACTTGCGAACTTGCGACTTGCGGACTTGCGACTTGCGAGACTTGCGCTTTACTTGCGGCAGGACTTGCGCCGGTCAACTTGCGACTCCACTTGCGGGCTACTTGCGTCACTTGCGAGTGGTTACTTGCGCAATGTAACTTGCGTCACTTGCGAACGCACTTGCGAGTGTCAGCGTGGAAACTTGCGAACTTGCGGGACTTGCGCATTACTTGCGGACTTGCGACTTGCGACTTGCGTAGAGTCCCGTAAACTTGCGGCCCCAGACTTGCGTACTTGCGAACAGACTTGCGCTAAGCACTTGCGAAAACTTGCGGCACTTGCGCACTTGCGTACTTGCGTAACCCAAAAAAAGCACTTGCGATGGTACTTGCGTCCGACACTTGCGCTCAACTTGCGAGACTTGCGACTTGCGAATTACTTGCGGACTTGCGACTTGCGCCCAGACTTGCGACTTGCGCGACGCTAACTTGCGCATACTTGCGAACTTGCGTCACTTGCGACTTGCGACTTGCGGAACGTCAGACTTGCGGACTTGCGCTACTTGCGATCACTGTAACTTGCGGAACTTGCGGACTTGCGCGTACTTGCGACTTGCGTATCACTTGCGACTTGCGAGCCACTTGCGGGGGACTTGCGACTTGCGCATAAAGTCACTTGCGGACTTGCGCGGACTTGCGACTTGCGCTGGATACTTGCGAGGACTTGCGAACTTGCGGTCACTTGCGATCACAACTTGCGCACTTGCGTCACTTGCGTTACTTGCGCACGCAAGCGTAACAGTACTTGCGTGTGTTTACTTGCGAACTTGCGAACTTGCGAATAC'

print(PatternCount('ACTGTACGATGATGTGTGTCAAAG', 'TGT'))

'''FrequentWords(Text, k)
        FrequentPatterns ← an empty set
        for i ← 0 to |Text| − k
            Pattern ← the k-mer Text(i, k)
            Count(i) ← PatternCount(Text, Pattern)
        maxCount ← maximum value in array Count
        for i ← 0 to |Text| − k
            if Count(i) = maxCount
                add Text(i, k) to FrequentPatterns
        remove duplicates from FrequentPatterns
        return FrequentPatterns
'''
    
def mostFrequent(text,k):
    freq_patterns = []
    count_list = []
    pattern_list = []
    for i in range(0,len(text)-k+1):
        pattern = text[i:i+k]
        pattern_list.append(pattern)
        count_list.append(PatternCount(text, pattern))
    maxCount = max(count_list)
    for i in range(0,len(count_list)):
        if count_list[i]==maxCount:
            if pattern_list[i] not in freq_patterns:
                freq_patterns.append(pattern_list[i])
    freq_patterns = sorted(freq_patterns)
    return freq_patterns

my_text = 'TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT'
my_k = 3
print(mostFrequent(my_text, my_k))

def int_to_string(list_int):
    list_str = []
    for item in list_int:
        list_str.append(str(item))
    return list_str

def reverse_complement(text):
    text = text.upper()
    complement_dict = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}
    comp = ''
    for i in range(len(text)):
        comp = comp + complement_dict[text[-i-1]]
    return comp

my_text_2 = 'GATTACA'
print(reverse_complement(my_text_2))
"""Code Challenge: Solve the Pattern Matching Problem.
     Input: Two strings, Pattern and Genome.
     Output: A collection of space-separated integers specifying all starting positions where Pattern appears
     as a substring of Genome."""
     
def pattern_matching(Pattern, Genome):
    index_string = ""
    for i in range(len(Genome)):
        if Genome[i:i+len(Pattern)] == Pattern:
            index_string = index_string + str(i) + " "
    return index_string

print(pattern_matching('CGC', 'ATGACTTCGCTGTTACGCGC'))
     
def clumper(Genome, k, L, t):
    """
    Clump Finding Problem: Find patterns forming clumps in a string.
    Input: A string Genome, and integers k, L, and t.
    Output: All distinct k-mers forming (L, t)-clumps in Genome.
    L: length of potential ori (within Genome)
    k: length of k-mer
    t: minimum number of times k-mer appears in L
    """
    kmers = []
    for i in range(len(Genome)-L+1):
        kmer_dict = {}
        for j in range(L-k+1):
            kmer = Genome[i+j:i+j+k]
            #cheat to make it faster
            if kmer not in kmers:
                if kmer in kmer_dict:
                    kmer_dict[kmer] = kmer_dict[kmer] + 1
                if kmer not in kmer_dict:
                    kmer_dict[kmer] = 1
        
        for key in kmer_dict:
            if kmer_dict[key] >= t:
                kmers.append(key)
    return kmers

def list_to_string(my_list):
    my_string = ""
    for item in my_list:
        my_string = my_string + item + " "
    return my_string

###Faster algorithm removes nested for loops
def faster_clumper(Genome, k, L, t):
    kmers = []
    kmer_dict = {}
    for j in range(L-k+1):
        kmer = Genome[j:j+k]
        if kmer in kmer_dict:
            kmer_dict[kmer] = kmer_dict[kmer] + 1
        if kmer not in kmer_dict:
            kmer_dict[kmer] = 1
        
    for key in kmer_dict:
        if kmer_dict[key] >= t:
            kmers.append(key)
   
    for i in range(len(Genome)-L):
        start_kmer = Genome[i:k+i]
        kmer_dict[start_kmer] = kmer_dict[start_kmer]-1
        end_kmer = Genome[i+L-k+1:i+L+1]
        if end_kmer in kmer_dict:
            kmer_dict[end_kmer] = kmer_dict[end_kmer] + 1
        if end_kmer not in kmer_dict:
            kmer_dict[end_kmer] = 1
        if kmer_dict[end_kmer] >= t and end_kmer not in kmers:
            kmers.append(end_kmer)
            
    return kmers


    
f = open('Ecoli.txt')
test = ''
for line in f:
    test = test + line
print(len(test))


easy_test = "abcabcdef"
B = (faster_clumper(easy_test, 3, 6, 2))
print(list_to_string(B))


A = (faster_clumper(test, 9, 500, 3))
print(len(A))    
     






