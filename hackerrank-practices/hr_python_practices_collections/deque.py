# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()

for _ in range(int(input())):
    ip = input().strip().split()
    if ip[0] == "append":
        d.append(ip[1])
    elif ip[0] == "pop":
        d.pop()
    elif ip[0] == "popleft":
        d.popleft()
    elif ip[0] == "appendleft":
        d.appendleft(ip[1])
print(' '.join(d))

