import itertools


def solution_1(A):  # gives 44% score
    max_product = A[0] * A[1] * A[2]

    for a, b, c in itertools.combinations(A, 3):
        if a * b * c > max_product:
            max_product = a * b * c
    return max_product


def solution(A):
    A.sort()
    n = len(A)
    obvious = A[n - 1] * A[n - 2] * A[n - 3]  # after lesson-6-sorting this might be the largest product
    max_product = max(obvious, A[0] * A[1] * A[n - 1])  # combination of first two (if first two are negative) and last
    # one
    return max_product


if __name__ == "__main__":
    _a = [-3, 1, 2, -2, 5, 6]
    print(solution(_a))
