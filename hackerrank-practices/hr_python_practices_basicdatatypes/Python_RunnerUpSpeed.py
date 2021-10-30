if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    unique = set()
    for i in arr:
        unique.add(i)
    unique = list(unique)
    unique.sort()
    print(unique[-2])
    #print(list(unique).sort()[-2])