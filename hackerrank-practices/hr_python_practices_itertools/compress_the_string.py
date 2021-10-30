from itertools import groupby

print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
# [list(g) for k, g in groupby('AAAABBBCCD')]
# output # (1, 1) (3, 2) (1, 3) (2, 1)
# S = "1222311"


