from collections import Counter

if __name__ == '__main__':
    s = input()
    c = Counter(sorted(s))
    coll_list = c.most_common(3)
    # print(coll_list)
    for i in range(len(coll_list)):
        print(*coll_list[i])

