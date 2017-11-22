#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:01:30 2017

@author: Susan Puckett
sepuckett86

Sorting Practice
"""
import time
import random

#define list of length n integers and print
def make_list(length):
    n = length
    int_list = []
    for i in range(n):
        int_list.append(i+1)
    return int_list

#define list of length n random integers and print
def make_ran(length):
    n = length
    int_list = []
    for i in range(n):
        int_list.append(random.randint(1,9))
    return int_list

#randomize a list and print
def randomize(list):
    random.shuffle(list)
    return list

#show elapsed time it takes to complete a function
def show_time(function, arg):
    start = time.time()
    out = function(arg)
    end = time.time()
    print("Time elapsed: %f" %(end - start) + " sec")
    return(end - start, out)

#bubble sort
def bubble_sort(a_list):
    ok = 0
    new_list = list(a_list)
    while ok < len(new_list)-1:
        ok = 0
        #print(new_list)
        for i in range(0,len(new_list)-1):
            if new_list[i] > new_list[i+1]:
                store = new_list[i]
                new_list[i] = new_list[i+1]
                new_list[i+1] = store
            else:
                ok += 1
    return new_list

#to use in merge sort
def merge_sort(a_list):
    
    # Divide the list into two `halves`
    n = len(a_list)
    #print(n)
    half_n = int(n/2)
    first_half = a_list[:half_n]
    second_half = a_list[half_n:]

    # Call mergesort on each of the halves
    if len(first_half) > 1:
        first_half = merge_sort(first_half)
        
    if len(second_half) > 1:
        second_half = merge_sort(second_half)
 
    # Merge the two sotrted halves into one list
    new_list = []
    new_list = merge(first_half,second_half)
        
    # Return the sorted whole list
    return new_list

    
def merge(list_a,list_b):
    index_a = 0
    index_b = 0
    merged_list = []
    while index_a < len(list_a) and index_b < len(list_b):
        if list_a[index_a] < list_b[index_b]:
            merged_list.append(list_a[index_a])
            index_a += 1
        elif list_a[index_a] > list_b[index_b]:
            merged_list.append(list_b[index_b])
            index_b += 1
        elif list_a[index_a] == list_b[index_b]:
            merged_list.append(list_a[index_a])
            merged_list.append(list_b[index_b])
            index_a += 1
            index_b += 1
    while index_a < len(list_a):
        merged_list.append(list_a[index_a])
        index_a += 1
    while index_b < len(list_b):
        merged_list.append(list_b[index_b])
        index_b += 1
    return merged_list    
        
    
#output
def format_result(sort_function, input_list, name):
    print("")
    print(name)
    print("First 10 in my_list: " + str((input_list[:10])))
    my_time, sorted_list = show_time(sort_function, input_list)
    print("First 50 in sorted_list: " + str((sorted_list[:50])))
    print("")

length = 1000
my_list = randomize(make_list(length))
print("For a list of length %d:" %length)

format_result(bubble_sort, my_list, "Bubble Sort")

format_result(merge_sort, my_list, "Merge Sort")

