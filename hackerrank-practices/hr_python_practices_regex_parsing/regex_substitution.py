# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())

for _ in range(N):
    text = input()
    while " && " in text or " || " in text:
        text = text.replace(" && ", " and ").replace(" || ", " or ")
    print(text)
