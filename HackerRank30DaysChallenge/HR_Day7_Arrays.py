import math
import os
import random
import re
import sys


if __name__ == '__main__':
    print('Enter inputs in two lines seperated by space.')
    print('Press enter and provide array input after first input')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print('You entered arrya with ',arr)
    reverse = map(str, arr[::-1])   #map function returns the iterable object. Here we converted int to string
    print(' '.join(reverse)) # Join function add seperator as space

