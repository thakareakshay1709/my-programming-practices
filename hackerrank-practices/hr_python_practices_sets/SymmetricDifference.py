n = int(input())
list1 = list(map(int,input().split()))
n1 = int(input())
list2 = list(map(int,input().split()))
[print(i) for i in sorted(set(list1).difference(set(list2)).union(set(list2).difference(set(list1))))]