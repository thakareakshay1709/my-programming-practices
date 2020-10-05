# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
no_shoes = int(input())
shoe_size = collections.Counter(map(int, input().split()))
cust_count = int(input())

money = 0
for i in range(cust_count):
    (size, cost) = map(int, input().split())
    if shoe_size[size] > 0:
        shoe_size[size] -= 1
        money = money + cost
print(money)
#
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50