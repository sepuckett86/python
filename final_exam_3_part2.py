#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:46:29 2017
Note: this code assumes only one longest ORF.
Part 2 of 2 coding files
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


#FOR GIVEN IDENTIFIER, LONGEST ORF

# Get identifier input from user
identifier_input = 0
i = 0

while i <= 5:
    if identifier_input not in identifier_list:
        identifier_input = input("Input identifier (example: gi|142022655|gb|EQ086233.1|160) here: ")
    if identifier_input not in identifier_list:
        print("This identifier not present. Try again.")
    else:
        input_seq_no = identifier_list.index(identifier_input)
        break
    i+=1
    
    
# Get reading frame input from user
# frame is python index number for frame (0, 1, or 2)
frame = False
# frame_input is user input frame (1, 2, 3, or all)
frame_input = 0
frame_list = ['1','2','3','all']
i = 0 
while i <= 5:
    if frame_input not in frame_list:
        frame_input = input("Input frame (1, 2, 3, or all) here: ")
    if frame_input not in frame_list:
        print("Frame unidentified. Try again.")
    if frame_input == 'all':
        frame = 'all'
        break
    elif frame_input == '1' or frame_input == '2' or frame_input == '3':
        frame = int(frame_input)-1
        break
    i+=1

# Determine ORF info in all or one frame
print(frame)
ORF_len = []
# For single frame
if frame == 0 or frame == 1 or frame == 2:
    ORF, start, stop = single_find_ORFS(DNA_list[input_seq_no],frame)
    for i in ORF: ORF_len.append(len(i))
    longest_ORF_len = max(ORF_len)
    print("The longest ORF length in reading frame %s is: %d bps."
          %(frame_input, longest_ORF_len))
    
    
# For all frames     
elif frame == 'all':
    ORF1, start1, stop1 = single_find_ORFS(DNA_list[input_seq_no],0)
    ORF2, start2, stop2 = single_find_ORFS(DNA_list[input_seq_no],1)
    ORF3, start3, stop3 = single_find_ORFS(DNA_list[input_seq_no],2)
    ORF = ORF1 + ORF2 + ORF3
    start = start1 + start2 + start3
    for i in ORF: ORF_len.append(len(i))
    longest_ORF_len = max(ORF_len)
    print("The longest ORF length in all reading frames is: " + str(longest_ORF_len)
    + " bps.")
    
#want dictionary with ORF length: ORF sequences with that length
len_ORF = {}
for x, y in zip(ORF, ORF_len):
    len_ORF.setdefault(y,[]).append(x)
#want dictionary of length:start
len_start = {}
for x, y in zip(start, ORF_len):
    len_start.setdefault(y,[]).append(x)

#determine longest ORF
longest_ORF_seq = len_ORF[longest_ORF_len] 
longest_ORF_seq_one = longest_ORF_seq[0]

#determine starting position of longest ORF
longest_start = len_start[longest_ORF_len]

#account for starting position: index 0 is position 1
longest_start_position = []
for x in longest_start:
    longest_start_position.append(x+1)
start_string = str(longest_start_position)
start_string = start_string[1:len(start_string)-1]
print("The starting position is: " + start_string)
print("The longest ORF starts with '%s' and ends with '%s'." %(longest_ORF_seq_one[:10], longest_ORF_seq_one[-10:]))


