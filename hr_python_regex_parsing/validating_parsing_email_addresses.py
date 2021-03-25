# Enter your code here. Read input from STDIN. Print output to STDOUT
from email import utils
import re

n = int(input())
pattern = re.compile(r"^[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$")
for i in range(n):
    valid_tup = utils.parseaddr(input())
    if pattern.match(valid_tup[1]):
        print(utils.formataddr((valid_tup[0], valid_tup[1])))