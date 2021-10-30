# cases = int(input())

cases = 2
set_A = set()
for i in range(cases):
    no_A = int(input())
    set_A = set(map(int, input().split()))
    no_B = int(input())
    set_B = set(map(int, input().split()))
    print(set_A.issubset(set_B))
