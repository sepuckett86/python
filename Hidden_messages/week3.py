#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 16:41:12 2018
week 3 Hidden Messages in DNA Coursera course
@author: Susan
"""


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

def match(string1, string2, d):
    """d is number of mismatches allowed
    """
    mismatches = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            mismatches += 1
        if mismatches > d:
            break
    if mismatches > d:
        return False
    else:
        return True

def make_DNA_list(dna_string):
    """takes a string of seqs with spaces and returns a list of those strings"""
    dna_list = dna_string.split()
    return dna_list

def motif(Dna, k, d):
    """
    Dna is a collection of strings
    k is the length of k-mer
    d is the number of accepted mismatches max
    
    We are interesting in knowing all k-mers that appear at least once per string, with d mismatches
    
    MotifEnumeration(Dna, k, d)
            Patterns ← an empty set
            for each k-mer Pattern in Dna
                for each k-mer Pattern’ differing from Pattern by at most d mismatches
                    if Pattern' appears in each string from Dna with at most d ﻿mismatches
                        add Pattern' to Patterns
            remove duplicates from Patterns
            return Patterns
       
    
    Example Input
    3 1
    ATTTGGC
    TGCCTTA
    CGGTATC
    GAAAATT
    
    Sample Output:
    
    ATA ATT GTT TTT
    """
    patterns = []
    kmer_list = []
    kmer_check = []
    mismatch = d
    # Identify kmers in first string in Dna
    for i in range(len(Dna[0])-k+1):
        kmer = Dna[0][i:k+i]
        kmer_list.append(kmer)
    kmer_check = kmer_list
    while mismatch > 0:
        # Generate mismatch list for kmer_list
        for item in kmer_list:
            kmer_list = mis_list(item)
            kmer_check = kmer_check + kmer_list
        kmer_list = kmer_check
        mismatch -= 1
    kmer_check = list(set(kmer_check))
    #For each kmer in kmer_check, see if it is in each string in Dna.
    print(kmer_check)
    for item in kmer_check:
        ok = True
        done = False
        while ok == True and done == False:
            for string in Dna:
                present = False
                for j in range(len(string)-k+1):
                    # Check for match in each position of string
                    if match(string[j:j+k],item,d) == True:
                        present = True
                        break
                    
                if present == False:
                    ok = False
            done = True
        if ok == True:
            patterns.append(item)
        
    # Remove duplicates
    patterns = list(set(patterns))
    return patterns

def quantify(long_string):
    """determines number of separate seqs in string"""
    seq_list = long_string.split()
    how_many = len(seq_list)
    return how_many

def list_to_string(my_list):
    my_string = ""
    for item in my_list:
        my_string = my_string + str(item) + " "
    return my_string

def score(Dna, kmer):
    """
    Given kmer, calculate d(Pattern, Dna). This is the sum of all mismatches of this
    kmer in each string, for its best match. 
    Input: list of Dna strings, kmer sequence
    Output: score, an integer. 
    """

    # Store list of scores, one for each string
    score_list = []
    
    for dna_string in Dna:
        # For one string, find where kmer matches the best. If there is more than one place, 
        # it doesn't matter which one is used to calulate the score. Trying for as low a score
        # as possible. 
        # Have x be the output of match function, starting as False
        x = False
        # Best match would be when d==0
        d = 0
        
        while x == False and d <= len(kmer):
            
            # Iterate over entire single Dna string
            for i in range(len(dna_string)-len(kmer)+1):
            
                string1 = dna_string[i:i+len(kmer)]
                
                string2 = kmer
                
                x = match(string1,string2,d)
                # Stop as soon as best match is found
                if x == True:
                    score_list.append(d)
                    break
           
            d += 1
        
    return sum(score_list)

def median_string(Dna, k):
    """
    Code Challenge: Implement MedianString.
     Input: An integer k, followed by a collection of strings Dna.
     Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all k-mers Pattern. (If there are
     multiple such strings Pattern, then you may return any one.)
     Sample Input:

    3
    AAATTGACGCAT
    GACGACCACGTT
    CGTCAGCGCCTG
    GCTGAGCACCGG
    AGTTCGGGACAG
    Sample Output:
    
    GAC
    
    Pseudocode
    MedianString(Dna, k)
        distance ← ∞
        for each k-mer Pattern from AA…AA to TT…TT
            if distance > d(Pattern, Dna)
                 distance ← d(Pattern, Dna)
                 Median ← Pattern
        return Median
     """
    # Generate list of kmers to test
    # I had to cheat here and put d == 3, although maybe we should check d == k - 1??
    kmer_list = motif(Dna, k, 3)
    
    score_list = []
    for kmer in kmer_list:
        a = score(Dna, kmer)
        score_list.append(a)
    minimum = min(score_list)
    indices = [i for i, x in enumerate(score_list) if x == minimum]
    final_kmers = []
    for index in indices:
        final_kmers.append(kmer_list[index])
    
    return final_kmers, minimum

''' Would a better way of doing this involve checking the first two strings? No.
    string 1: 'AAAA'
    string 2: 'AAAB'
    string 3: 'DDDD'
    string 4: 'DDDD'
    score(list, 'AAAA') = 9
    score(list, 'AAAB') = 9
    score(list, 'DDDD') = 8
'''


    
def input_profile(filename):
    '''
    Input: filename of of file to process for profile function
    Output: Text, k, matrix_dict
    '''
        
    file_list = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            file_list.append(line.strip())
    file_list[1] = int(file_list[1])
    matrix_dict = {}
    matrix_dict['A'] = file_list[2].split()
    # Convert list of strings into list of floating point values
    matrix_dict['A'] = [float(i) for i in matrix_dict['A']]
    matrix_dict['C'] = file_list[3].split()
    matrix_dict['C'] = [float(i) for i in matrix_dict['C']]
    matrix_dict['G'] = file_list[4].split()
    matrix_dict['G'] = [float(i) for i in matrix_dict['G']]
    matrix_dict['T'] = file_list[5].split()
    matrix_dict['T'] = [float(i) for i in matrix_dict['T']]

    Text = file_list[0]
    k = file_list[1]

    '''
    Text = list_of_lists[0]
    k = list_of_lists[1]
    matrix_dict = {}
    matrix_dict['A'] = list_of_lists[2].split()
    matrix_dict['C'] = list_of_lists[3].split()
    matrix_dict['G'] = list_of_lists[4].split()
    matrix_dict['T'] = list_of_lists[5].split()
    '''
    return Text, k, matrix_dict
   
    
def profile(Text, k, matrix_dict):
    '''
    Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.
     Input: A string Text, an integer k, and a 4 × k matrix Profile.
     Output: A Profile-most probable k-mer in Text.
    '''
    profile_list = []
    kmer_list = []
    # Loop through all kmers of length k in Text
    for i in range(len(Text)-k+1):
        kmer = Text[i:i+k]
        kmer_list.append(kmer)
    # Calculate profile for given string
    # k is length of string, matrix_dict is profile matrix
        profile = 1
        for j in range(k):
            number = matrix_dict[kmer[j]][j]
            profile = profile * number
        profile_list.append(profile)
    print(profile_list)
    maximum = max(profile_list)
    indices = [i for i, x in enumerate(profile_list) if x == maximum]
    first_kmer = kmer_list[indices[0]]
    print(kmer_list)
    return first_kmer

text, k, matrix = input_profile("test.txt")

def greedy(Dna, k, t):
    """
    Dna is a list of t (integer) strings, each of some arbitrary length > k (integer)
    Concept: 1) test all kmers in first string for k-mer with the lowest profile score.
             2) identify indices of all the best matches to this kmer, one per string
             3) return a list of these kmers.
    Input example:
    3 5
    GGCGTTCAGGCA
    AAGAATCAGTCA
    CAAGGAGTTCGC
    CACGTCAATCAC
    CAATAATATTCG
    Output example:
    CAG
    CAG
    CAA
    CAA
    CAA
    """
    sc_list = []
    kmer_list = []
    for i in range(len(Dna[0])-k+1):
        kmer = Dna[0][i:i+k]
        sc = score(Dna,kmer)
        sc_list.append(sc)
        kmer_list.append(kmer)
    print(sc_list)
    minimum = min(sc_list)
    indices_min = [i for i, x in enumerate(sc_list) if x == minimum]
    best_kmer = kmer_list[indices_min[0]]
    
    # Edit score function to fit our purposes
    # Store best kmers, 1 per string, here:
    best_kmer_list = [best_kmer]
    
    for dna_string in Dna[1:]:
        # For each string, find where best_kmer matches the best. If there is more than one place,
        # return the first one.
        # as possible. 
        # Have x be the output of match function, starting as False
        x = False
        # Best match would be when d==0
        d = 0
        
        while x == False and d <= len(kmer):
            
            # Iterate over entire single Dna string
            for i in range(len(dna_string)-len(kmer)+1):
            
                string1 = dna_string[i:i+len(kmer)]
                
                string2 = kmer
                
                x = match(string1,string2,d)
                # Stop as soon as best match is found
                if x == True:
                    best_kmer_list.append(dna_string[i:i+len(kmer)])
                    break
           
            d += 1
    return best_kmer_list
        
    
dna_list = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
print(greedy(dna_list, 3, 5))