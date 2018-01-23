#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:52:49 2017
1.2 Hidden messages in the Replication Origin
Week Two
Coursera class
@author: Susan
"""



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
    for i in range(1,len(Genome)+1):
        if Genome[i-1] == 'C':
            n -= 1
        if Genome[i-1] == 'G':
            n += 1
        skew_out = skew_out + ' ' + str(n)
    return skew_out




def skew_min(Genome):
    '''
    Minimum Skew Problem: Find a position in a genome where the 
    skew diagram attains a minimum.
    Input: A DNA string Genome.
    Output: All integer(s) i minimizing Skewi (Genome) among 
    all values of i (from 0 to |Genome|).
    '''
    skew_list = [0]
    n = 0
    for i in range(1,len(Genome)+1):
        if Genome[i-1] == 'C':
            n -= 1
        if Genome[i-1] == 'G':
            n += 1
        skew_list.append(n)
    minimum = min(skew_list)
    print(minimum)
    indices = [i for i, x in enumerate(skew_list) if x == minimum]
    return indices

def list_to_string(my_list):
    my_string = ""
    for item in my_list:
        my_string = my_string + str(item) + " "
    return my_string



def hamming(str1, str2):
    '''
    Hamming Distance Problem: Compute the Hamming distance between two strings.
    Input: Two strings of equal length.
    Output: The Hamming distance between these strings.
    Hamming distance is the number of mismatches
    '''
    n = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            n += 1
    return n


def approx(Pattern, Text, d):
    """
    Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
     Input: Strings Pattern and Text along with an integer d.
     Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
    """
    start_positions = ''
    for i in range(len(Text)-len(Pattern)+1):
        if hamming(Text[i:i+len(Pattern)], Pattern) <= d:
            start_positions = start_positions + str(i) + ' '
    return start_positions

def str_to_list(str1):
    '''
    Takes string with space separated values and returns a list made up of those values
    '''
    myList = str1.split()
    return myList

def approx_patt_count(Pattern, Text, d):
    '''
    Code Challenge: Implement ﻿ApproximatePatternCount.
     Input: Strings Pattern and Text as well as an integer d.
     Output: Countd(Text, Pattern). --the number of patterns allowing for d mismatches
    '''
    myList = str_to_list(approx(Pattern, Text, d))
    return len(myList)

p1 = 'GTGAAT'
t1 = 'CTCTTCGATGCATGTTAGAGCCGGCAGTTCTATCCCCGACACCTTCACGTCTTTATTGGAGGGGACGTATTTTCCCATTTCCAATTACCCTTCTCTTCCAAATAAGCAAGTGAATAACTGTCCTGCGCGATTATATAACAGCGTTTCTGTGGTTCGCATCAAATGGGCGGGCGGTAAAGGCTGTGTAGGCCGCCGCTCGCAATGCGTGGGTGCCTGAGTTGTACCCACAACGGACCGCATGTATCCTCTATCGTGCAGATATCTCTAAGGCGCCCTTACCGAGATGGGTGAGAATGTCTACTATTTAATTAGAGGAGAATTTGGTTTGCGAACGTTGTTGGGTCATATTCAACCCCGGACTCCTATAGGAAGCGACATCCT'
d1 = 3

    
def most_freq(Text, k, d):
    '''Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
     Output: All most frequent k-mers with up to d mismatches in Text.
    '''
    kmer_list = []
    kmer_count_list = []
    final_kmer_list = []
    for i in range(len(Text)-k+1):
        kmer = Text[i:i+k]
        kmer_list.append(kmer)
        count = approx_patt_count(kmer, Text, d)
        kmer_count_list.append(count)
    maximum = max(kmer_count_list)
    indices = [i for i, x in enumerate(kmer_count_list) if x == maximum]
    for x in indices:
        if kmer_list[x] not in final_kmer_list:
            final_kmer_list.append(kmer_list[x])
    return list_to_string(final_kmer_list)
      


def mis_list(kmer):
    '''
    make list of kmers with one mismatch from a single kmer
    '''
    base_options = ['A','T','G','C']
    kmer_mis = []
    for i in range(len(kmer)):
        for base in base_options:
            kmer_1 = kmer[:i] + base + kmer[i+1:]
            if kmer_1 != kmer:
                kmer_mis.append(kmer_1)
    kmer_mis = list(set(kmer_mis))
    return kmer_mis

def PatternCount(text, pattern):
    count = 0
    for i in range (0, len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

def freq_with_mismatches(Text, k, d):
    '''Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
     Output: All most frequent k-mers with up to d mismatches in Text.
     NOTE: kmer does not have to appear within text.
     1) Define list of kmers to check
        -all kmers in text plus those kmers with d mismatches
     2) Check list of kmers against text allowing for mismatches
        -quantify how many times each appears in text
     3) Find top matches and return string of them separated by spaces
        -challenge: get the correct order that matches with course.
    '''
    # Define list of kmers to check
    kmer_check = []
    for i in range(len(Text)-k+1):
        kmer = Text[i:i+k]
        kmer_check.append(kmer)
        # Find kmers with up to d mismatches
        kmer_list = [kmer]
        mismatch = d
        while mismatch > 0:
            # Generate mismatch list for kmer_list
            for item in kmer_list:
                kmer_list = mis_list(item)
                kmer_check = kmer_check + kmer_list
            mismatch -= 1
            
    # Find unique items
    kmer_check = list(set(kmer_check))
    print(kmer_check)

    # Quantify how many times each kmer in kmer_check matches in Text
    kmer_count_list = []
    for kmer in kmer_check:
        kmer_count_list.append(approx_patt_count(kmer, Text, d))
        
    print (kmer_count_list)
    
    # Find max counts
    maximum = max(kmer_count_list)
    indices = [i for i, x in enumerate(kmer_count_list) if x == maximum]
    kmer_string = ''
    for index in indices:
        kmer_string = kmer_string + kmer_check[index] + ' '
        
    return kmer_string

def reverse_complement(text):
    text = text.upper()
    complement_dict = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}
    comp = ''
    for i in range(len(text)):
        comp = comp + complement_dict[text[-i-1]]
    return comp

def reverse(Text, k, d):
    '''
    Frequent Words with Mismatches and Reverse Complements Problem: 
        Find the most frequent k-mers (with mismatches and reverse complements) in a string.
      Input: A DNA string Text as well as integers k and d.
      Output: All k-mers Pattern maximizing the sum Countd(Text, Pattern)+ 
          Countd(Text, Patternrc) over all possible k-mers.
    '''
    # Define list of kmers to check
    kmer_check = []
    for i in range(len(Text)-k+1):
        kmer = Text[i:i+k]
        kmer_check.append(kmer)
        # Find kmers with up to d mismatches
        kmer_list = [kmer]
        mismatch = d
        while mismatch > 0:
            # Generate mismatch list for kmer_list
            for item in kmer_list:
                kmer_list = mis_list(item)
                kmer_check = kmer_check + kmer_list
            mismatch -= 1
            
    # Find unique items
    kmer_check = list(set(kmer_check))

    # Reverse complement
    kmer_check_reverse = []
    for item in kmer_check:
        kmer_check_reverse.append(reverse_complement(item))
        
    # Quantify how many times each kmer in kmer_check matches in Text
    kmer_count_list = []
    for kmer in kmer_check:
        kmer_count_list.append(approx_patt_count(kmer, Text, d))
        
    # Quantify how many times each kmer in kmer_check_reverse matches in Text
    kmer_count_list_reverse = []
    for kmer in kmer_check_reverse:
        kmer_count_list_reverse.append(approx_patt_count(kmer, Text, d))
    
    # Add lists
    added_list = []
    for i in range(len(kmer_count_list)):
        added_list.append(kmer_count_list[i]+kmer_count_list_reverse[i])
        
    # Find max counts
    maximum = max(added_list)
    indices = [i for i, x in enumerate(added_list) if x == maximum]
    kmer_string = ''
    for index in indices:
        kmer_string = kmer_string + kmer_check[index] + ' '
        
    return kmer_string

def neighbors(Pattern,d):
    '''
    Code Challenge: Implement Neighbors to find the d-neighborhood of a string.
     Input: A string Pattern and an integer d.
     Output: The collection of strings Neighbors(Pattern, d). (You may return the strings in any order, but each line should contain
     only one string.)
    '''
    mis = d
    # list of strings to look for 1 mismatch
    kmer_list = [Pattern]
    # list of kmer mismatches that are for per kmer in kmer_list
    item_list = []
    # list of kmer mismatches for all kmers in kmer_list
    round_list = []
    final = [Pattern]
    while mis > 0:
        for kmer in kmer_list:
            item_list = mis_list(kmer)
            round_list = round_list + item_list
        kmer_list = round_list
        final = final + round_list
        mis -= 1
        
    # Find unique items
    final = list(set(final))
    
    for item in final:
        print(item)
    print(len(final))

