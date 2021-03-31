# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = "aaadaa"  # input()
k = "aa"  # input()

pattern = re.compile(k)
r = pattern.search(s)
if not r: print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(s, r.start() + 1)
