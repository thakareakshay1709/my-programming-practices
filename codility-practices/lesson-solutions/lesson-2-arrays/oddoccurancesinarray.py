def solution(A):
    unpaired = set()
    for i in A:
        if i in unpaired:
            unpaired.remove(i)
        else:
            unpaired.add(i)
    print(unpaired)
    result = unpaired.pop()
    return result
    # SOl - partial correct
    # S = set(A)
    # # print(S)
    #
    # for s in S:
    #     count = 0
    #     for a in A:
    #         if s == a:
    #             count += 1
    #     if count == 1:
    #         return s


if __name__ == "__main__":
    _A = [9, 3, 9, 3, 9, 7, 9]
    print(solution(_A))
