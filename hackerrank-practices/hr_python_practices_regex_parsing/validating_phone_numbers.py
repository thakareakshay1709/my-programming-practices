import re

N = int(input())
pattern = r"^[7-9]\d{9}$"
for _ in range(N):
    found = bool(re.match(pattern, input()))
    if found:
        print('YES')
    else:
        print('NO')
