def solution(A, K):
    # print(A, K)
    if len(A) == 0:
        return []
    new = [0] * len(A)
    for i in range(K):
        new[0] = A[-1]
        new[1:] = A[:-1]
        A = new.copy()
    return A


if __name__ == "__main__":
    _A = [3, 8, 9, 7, 6]
    _K = 3
    print(solution(_A, _K))
