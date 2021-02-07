# Enter your code here. Read input from STDIN. Print output to STDOUT
# -*- coding: utf-8 -*-
import math
AB = int(input())
BC = int(input())

print(str(round(math.degrees(math.atan2(AB, BC))))+'°')
