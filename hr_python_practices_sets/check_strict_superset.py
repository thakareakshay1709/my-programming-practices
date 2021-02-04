# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = set(map(int, input().split()))
n, count = int(input()), 0
#print(set_a, n)
for i in range(n):
    set_b = set(map(int, input().split()))
    if set_a.issuperset(set_b):
        count+= 1
print(n == count)
