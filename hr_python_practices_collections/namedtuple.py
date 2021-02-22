from collections import namedtuple
n = int(input())
Scorer = namedtuple('Scorer', input().split())
scores = [Scorer(*input().split()).MARKS for i in range(n)]
print("%.2f"% (sum(map(int,scores))/n))