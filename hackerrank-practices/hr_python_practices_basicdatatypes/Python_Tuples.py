if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_list = list(integer_list)
    print(integer_list)
    tup = ()
    for i in range(len(integer_list)):
        tup = tup + (integer_list[i],)
    print(hash(tup))