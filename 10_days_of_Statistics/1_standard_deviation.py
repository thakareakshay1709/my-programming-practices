# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from math import sqrt
n,x = int(input()), list(map(int, input().split()))

avg = np.mean(x)
sqr_dis = 0

for i in range(n):
    sqr_dis += ((x[i] - avg)**2)

print(round(sqrt(sqr_dis/n),1))