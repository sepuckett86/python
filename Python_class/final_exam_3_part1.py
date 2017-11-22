#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:42:36 2017
@author: Susan Puckett
Python script made using Spyder
This script answers question #3 for the Coursera class final project
Genomic Data Science -- Python
Question: 
    "(3) In molecular biology, a reading frame is a way of dividing the 
    DNA sequence of nucleotides into a set of consecutive, non-overlapping 
    triplets (or codons). Depending on where we start, there are six 
    possible reading frames: three in the forward (5' to 3') direction and
    three in the reverse (3' to 5'). For instance, the three possible 
    forward reading frames for the sequence AGGTGACACCGCAAGCCTTATATTAGC are:

        AGG TGA CAC CGC AAG CCT TAT ATT AGC

        A GGT GAC ACC GCA AGC CTT ATA TTA GC

        AG GTG ACA CCG CAA GCC TTA TAT TAG C

    These are called reading frames 1, 2, and 3 respectively. 
    An open reading frame (ORF) is the part of a reading frame that has the 
    potential to encode a protein. It starts with a start codon (ATG), and 
    ends with a stop codon (TAA, TAG or TGA). For instance, ATGAAATAG is an 
    ORF of length 9.

    Given an input reading frame on the forward strand (1, 2, or 3) your 
    program should be able to identify all ORFs present in each sequence 
    of the FASTA file, and answer the following questions: what is the 
    length of the longest ORF in the file? What is the identifier of the 
    sequence containing the longest ORF? For a given sequence identifier, 
    what is the longest ORF contained in the sequence represented by that 
    identifier? What is the starting position of the longest ORF in the 
    sequence that contains it? The position should indicate the character 
    number in the sequence. For instance, the following ORF in reading 
    frame 1:

        >sequence1

        ATGCCCTAG

        starts at position 1.

        Note that because the following sequence:

        >sequence2

        ATGAAAAAA

        does not have any stop codon in reading frame 1, we do not consider 
        it to be an ORF in reading frame 1."

Part 1 of 2 coding files
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

#QUESTION 3
#Identify ORFs in the forward strand in inputted reading frame
#ORF defined as starting with ATG and ending with TAA, TAG, or TGA in same reading frame

def single_find_ORFS(seq, frame):
    """
    Finds ORFs in one input sequence.
    Input:  DNA sequence, reading frame 0, 1, or 2
    Output: three lists
                ORF_list = ORFs
                start_list = ORF start indicies
                stop_list = ORF stop indicies
        
    """
    start_list = []
    stop_list = []
    #for loop divides seq into groups of 3 characters for codons
    for i in range(frame, len(seq), 3):
        codon = seq[i:i+3]
        #if loop tests for start codon 'ATG'
        if codon == 'ATG':
            #for loop divides seq from start codon on into codons
            for j in range(i+3, len(seq), 3):
                codon2 = seq[j:j+3]
                stop_codons = ['TAA','TAG','TGA']
                #if loop searches for stop codon in frame with start codon
                if codon2 in stop_codons:
                    #record position of start codon
                    start_list.append(i)
                    #record position of last base in stop codon
                    stop_list.append(j+3)
                    break

    #make dictionary of start and stop positions
    start_stop = dict(zip(start_list, stop_list))

    #make list of all ORFs in all 3 reading frames
    ORF_list = []
    for index in start_list:
        ORF_list.append(seq[index:start_stop[index]])
    
    #return dictionary of {ORF: starting position}
    return (ORF_list, start_list, stop_list)
    
def all_longest_ORFs (DNA_list, frame):
    """
    Finds ORFs in all sequences, longest ORF in each sequence.
    Input:  DNA_list of sequences, reading frame of interest.
    Output: list: the longest ORFs in each sequence, integer: the longest ORF length in all sequences
    """
    all_longest = []
    # For loop to cycle through each sequence in DNA_list
    for x in DNA_list:
        # Find ORFs using find_ORFs function
        ORF_list, start_list, stop_list = single_find_ORFS(x,frame)
        # Find lengths of ORFs
        ORF_lengths = []
        for y in ORF_list:
            ORF_lengths.append(len(y))
        # Want dictionary with ORF length: number of ORFs with that length
        d = {}
        for z in ORF_lengths:
            if z in d:
                d[z] +=1
            else:
                d[z] = 1
        # Find longest ORF from this sequence
        if ORF_lengths != []:
            longest = max(ORF_lengths)
        else: 
            longest = 0
        # Store longest in master list
        all_longest.append(longest)
    the_longest = max(all_longest)
    return (all_longest, the_longest)

# Find longest ORF in all sequences and ORF identifier 
# Ask user to input frame
done = False
while done == False:
    frame_input = input("Input reading frame of interest (1, 2, 3, or all) here: ")
    # For a specified frame
    frame_list = ['1','2','3']
    if frame_input in frame_list:
        frame = int(frame_input)-1
        all_longest, the_longest = all_longest_ORFs(DNA_list, frame)
        the_longest = the_longest
        print("The length of the longest ORF in all sequences in frame %s is %d: " 
              %(frame_input, the_longest))
        # Make dictionary of (longest ORF length: identifier)
        longest_iden = {}
        for x, y in zip(identifier_list, all_longest):
            longest_iden.setdefault(y,[]).append(x)
        print("The identifier of the seq with longest ORF: " + str(longest_iden[the_longest]))
        done = True
    # For all frames
    elif frame_input == 'all':
        longest_1, the_1 = all_longest_ORFs(DNA_list, 0)
        longest_2, the_2 = all_longest_ORFs(DNA_list, 1)
        longest_3, the_3 = all_longest_ORFs(DNA_list, 2)
        all_longest = longest_1 + longest_2 + longest_3
        all_identifiers = identifier_list*3
        the_longest = max(all_longest)
        print("The length of the longest ORF in all sequences in all frames is: %d " 
              %the_longest)
        # Make dictionary of (longest ORF length: identifier)
        longest_iden = {}
        for x, y in zip(all_identifiers, all_longest):
            longest_iden.setdefault(y,[]).append(x)
        print("The identifier of the seq with longest ORF in all frames is: " 
              + str(longest_iden[the_longest]))
        done = True
    else:
        print("Cannot understand input. Try again.")


