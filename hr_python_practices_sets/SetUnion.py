e = int(input())
s_e = set(map(int, input().split()))
f = int(input())
s_f = set(map(int, input().split()))


print(len(s_e.union(s_f)))