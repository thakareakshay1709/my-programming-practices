#!/usr/bin/env python
# coding: utf-8

# #Hacker Rank Day 6#
# 
# Objective
# Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!
# 
# Task
# Given a string, S , of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).
# Note: 0 is considered to be an even index.
# 
# Input Format
# 
# The first line contains an integer, T (the number of test cases).
# Each line i of the T subsequent lines contain a String,S.
# 
# Constraints
# 
# 1 <= T <= 10
# 2 <= S <= 10000
# 
# Output Format
# 
# For each String Sj (where 0<= j <= T-1), print Sj's even-indexed characters, followed by a space, followed by Sj's odd-indexed characters.
# 
# Sample Input
# 
# 2
# Hacker
# Rank
# 
# Sample Output
# 
# Hce akr
# Rn ak

# In[1]:



TestCases = int(input())

for i in range(TestCases):
    inputString = input()
    evenString = inputString[0::2] #slicing string from 0th location till end [0:], and skipping with the difference of 2 [0::2]
    oddString = inputString[1::2] ##slicing string from 1st location till end [1:], and skipping with the difference of 2 [0::2]
    print(evenString+" "+oddString)
 

