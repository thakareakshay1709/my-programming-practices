import math
import os
import random
import re
import sys


def getConsecutiveOnes(n):
    binaryNum = bin(n)
    binwopfx = str(binaryNum)
    binwopfx = binwopfx[2:]
    print("Binary representation of %d = %s" %(n,binwopfx))
    countOnes = 0
    maxOnes = 0

    for elements in binwopfx:
        if int(elements) == 1:
            countOnes+= 1
            maxOnes = max(maxOnes,countOnes)
        else:
            countOnes = 0
    print("Consective Ones in %s = %d" % (binwopfx, countOnes))
    return maxOnes


if __name__ == '__main__':
    n = int(input("Enter number"))
    #print(n)
    consecutiveOnes = getConsecutiveOnes(n)
    print(consecutiveOnes)