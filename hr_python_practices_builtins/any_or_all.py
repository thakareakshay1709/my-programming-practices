n = int(input())
n_s = input().split()

print(all([int(j) >= 0 for j in n_s]) and any([k == k[::-1] for k in n_s]))
