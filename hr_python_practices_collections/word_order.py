# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

distinct_words = OrderedDict()

for n in range(int(input())):
    each_word = input()
    distinct_words.setdefault(each_word, 0)
    distinct_words[each_word] += 1

print(len(distinct_words))
print(*distinct_words.values())