# Enter your code hre. Read input from STDIN. Print output to STDOUT
# import statistics
# from
# no = input()
# array = sorted(list(map(int, input().split())))

# print(statistics.mean(array))
# print(statistics.median(array))
# print(statistics.mode(array))
import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print( int(stats.mode(numbers)[0]) )
