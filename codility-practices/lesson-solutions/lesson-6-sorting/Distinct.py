def solution_1(A):  # give 100 score
    return len(set(A))


def solution(A):
    l = []
    count = 0
    for i in A:
        if i not in l:
            l.append(i)
            count+=1
    return count


if __name__ == "__main__":
    _a = [2, 1, 1, 2, 3, 1]
    print(solution(_a))
