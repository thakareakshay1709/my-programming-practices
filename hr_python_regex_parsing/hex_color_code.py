# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
# color_code = r"(?<!^)(#(?:[\da-fA-F]{3}){1,2})"
new_code = r":?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})"
for i in range(n):
    m = re.findall(new_code, input())
    if m:
        print(*m, sep='\n')