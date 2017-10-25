#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:17:00 2017
Week 1 assignment

'First, implement a version of the naive exact matching algorithm 
that is strand-aware. That is, instead of looking only for 
occurrences of P in T, additionally look for occurrences of 
thereverse complement of P in T. If P is ACT, your function 
should find occurrences of both ACTand its reverse complement AGT
 in T.

If P and its reverse complement are identical (e.g. AACGTT), 
then a given match offset should be reported only once. So if 
your new function is called naive_with_rc, then the old 
naivefunction and your new naive_with_rc function should return 
the same results when P equals its reverse complement.'

@author: Susan
"""

def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences

def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t


def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome


def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

# HW Make function naive_with_rc

def naive_with_rc (p, t):
    rev_p = reverseComplement(p)
    if rev_p != p:
        occurrencesReverse = naive(rev_p, t)
    else:
        occurrencesReverse = []
    occurrencesForward = naive(p, t)
    if occurrencesReverse != []:
        all_occurrences = sorted(occurrencesForward + occurrencesReverse)
    else:
        all_occurrences = sorted(occurrencesForward)
    return all_occurrences

# Parse lambda virus genome
lambda_genome = readGenome('lambda_virus.fa')
occurrences = naive_with_rc('AGTCGA', lambda_genome)
print(occurrences)
print('offset of leftmost occurrence: %d' % min(occurrences))
print('# occurrences: %d' % len(occurrences))
      
# HW 5: Make naive_2mm function, no reverse complement, allow up to 2 mismatches
def naive_2mm(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        mismatch = 0
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                mismatch += 1
            if mismatch == 3:
                break
        if mismatch < 3:
            occurrences.append(i)  # all chars matched; record
    return occurrences

lambda_genome = readGenome('lambda_virus.fa')
occurrences = naive_2mm('AGGAGGTT', lambda_genome)
print('offset of leftmost occurrence: %d' % min(occurrences))
print('# occurrences: %d' % len(occurrences))
      
# Q 7: finding quality scores that are bad
seqs, quals = readFastq('hello.fastq')
      
def phred33ToQ(qual):
    return ord(qual) - 33
      
def createHist(qualities):
    hist = [0] * 50
    for qual in qualities:
        for phred in qual:
            q = phred33ToQ(phred)
            hist[q] += 1
    return hist
h = createHist(quals)



# Make list in order of index of max quality score for that index
# Did not use this function that finds the most frequent quality numbser
# for each position
def max_qual(quals):
    import collections
    master_quals = []
    # loop over each character in seq
    for j in range(len(quals[0])):
        qual_list_for_char = []
        # loop over all seqs
        for i in range(len(quals)):
            score_seq = quals[i]
            char = score_seq[j]
            score = phred33ToQ(char)
            qual_list_for_char.append(score)   
        count = collections.Counter()
        count.update(qual_list_for_char)
        print (count)
        max_score = max(count, key=count.get)
        master_quals.append(max_score)
    return master_quals

# Used this function which finds number of quality score 2 per character
def low_qual(quals):
    master_quals = []
    # loop over each character in seq
    for j in range(len(quals[0])):
        qual_two = 0
        # loop over all seqs
        for i in range(len(quals)):
            score_seq = quals[i]
            char = score_seq[j]
            score = phred33ToQ(char)
            if score == 2:
                qual_two +=1
        master_quals.append(qual_two)
    return master_quals

h = low_qual(quals)
print(h)
import matplotlib.pyplot as plt
plt.bar(range(len(h)), h)
plt.show()

index = h.index(max(h))
print (index)