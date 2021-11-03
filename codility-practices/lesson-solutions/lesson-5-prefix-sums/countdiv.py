def solution_2(A, B, K):  # partial solution with overall score of 50 with correctness 100
    count = 0
    for i in range(A, B + 1):
        if i % K == 0:
            count += 1
    return count


def solution(A, B, K):
    # print(B/K)
    r = B//K - A//K
    if A%K == 0:
        r += 1
    return r


if __name__ == "__main__":
    _A, _B, _K = 6, 11, 2
    print(solution(_A, _B, _K))
