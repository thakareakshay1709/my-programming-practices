from itertools import permutations
string, k = input().split()
permuts = list(permutations(string, int(k)))
# print(sorted(permuts))
for permut in sorted(permuts):
    print(''.join(permut))