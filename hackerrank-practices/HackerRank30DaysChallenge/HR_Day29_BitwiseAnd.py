#!/bin/python3

import math
import os
import random
import re
import sys


def bitwise(n, k):
    # print(n,k)
    max_value = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i is not j:
                print(i & j)
                if i & j < k:
                    max_value = max(i & j, max_value)
    print(max_value)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        bitwise(n, k)
