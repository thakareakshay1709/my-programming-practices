#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
def bubbleSort(a, n):
    #print("Array = ",a)
    #print("Total Elements =",n)

    totalSwaps = 0
    for i in range(0,n):

        for j in range(0,n-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                totalSwaps+=1
        if totalSwaps == 0:
            break;

    print("Array is sorted in %d swaps."%totalSwaps)
    print("First Element:", a[0])
    print("Last Element:", a[len(a)-1])


bubbleSort(a,n)