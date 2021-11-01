def solution_2(A):  # solution with partial test cases passed and performance is 100%
    A.sort(reverse=True)  # sorting in decending order

    if len(A) == 1:  # edge case
        return 1
    for i in range(len(A)):  # iterate over all elements
        if i + 1 < len(A):
            if A[i] - 1 == A[i + 1]:  # check if next element is less than 1
                continue
            else:
                return 0
    return 1


def solution(A):  # passed with all test cases and performance
    expected_sum = sum(range(1, len(A) + 1))
    # print(expected_sum)
    actual_sum = sum(A)
    # print(actual_sum)
    if len(set(A)) != len(A):
        return 0
    if expected_sum - actual_sum != 0:
        return 0
    return 1


if __name__ == "__main__":
    _A = [4, 1, 3]
    print(solution(_A))
