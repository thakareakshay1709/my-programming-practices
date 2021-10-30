import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    hourGlasses = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    sumHourGlass = 0
    maxSum = 0
    #print(len(arr))
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            #print(arr[row][col],sep=' ',end='\t') arr[0][0] arr[0][1] arr[0][2]
            #print(arr[row][col],sep=' ',end='\t')           arr[1][1]
            #print(arr[row][col],sep=' ',end='\t') arr[2][0] arr[2][1] arr[2][2]
            if(row + 2 < len(arr) and col+2 < len(arr)):
                sumHourGlass = arr[row][col] + arr[row][col+1] + arr[row][col+2] + arr[row+1][col+1] +\
                           arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
                maxSum = max(maxSum,sumHourGlass)
    print(maxSum)
