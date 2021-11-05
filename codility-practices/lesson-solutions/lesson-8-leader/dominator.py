import statistics


def solution(A):
    n = len(A)
    _mode = statistics.mode(A)
    print(_mode)
    if _mode != A[n // 2]:
        return -1
    for i in A:
        if i == _mode:
            return i


if __name__ == "__main__":
    _a = [3, 2, 3, 4, 3, 3, 3, -1]
    print(solution(_a))
