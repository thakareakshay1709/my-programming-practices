def solution(A):
    if len(A) == 1:
        return 1

    smallest_int = 1
    smallest_set = set(A)
    print(smallest_set)
    while smallest_int in smallest_set:
        smallest_int += 1
    return smallest_int


if __name__ == "__main__":
    _A = [-1,-3]
    print(solution(_A))
