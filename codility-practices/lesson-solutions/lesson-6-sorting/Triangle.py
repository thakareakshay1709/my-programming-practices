import itertools


# def solution(A):
#     for a, b, c in itertools.combinations(A, 3):
#         if a + b > c or a + c > b or b + c > a:
#             return 1
#     return 0

def solution(A):
    n = len(A)

    if n < 3:
        return 0

    A.sort()
    for i in range(n-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1

    return 0


if __name__ == "__main__":
    _a = [10, 50, 5, 1]  # 10, 50, 5, 1
    print(solution(_a))
