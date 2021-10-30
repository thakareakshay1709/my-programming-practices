def average(array):
    # your code goes here
    # print(len(array))
    dis = set()
    [dis.add(distinct) for distinct in array]
    return sum(dis) / len(dis)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
