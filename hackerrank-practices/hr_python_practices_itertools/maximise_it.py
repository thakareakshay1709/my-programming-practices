_ = input().split()
k = int(_[0])
m = int(_[1])
sqr = 0
for i in range(k):
    list_n = sorted(list(map(int, input().split())), reverse=True)
    sqr += list_n[0]**2
print(sqr % m)

### Learn this
# from itertools import product
#
# K,M = map(int,input().split())
# N = (list(map(int, input().split()))[1:] for _ in range(K))
# results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
# print(max(results))