def solution(A, X):  # partially correct solution
    if X < 1 or len(A) < 1:
        return -1
    lista = list(range(1, X + 1))
    print(lista)
    found = -1
    for e in lista:
        if e in A:
            if A.index(e) > found:
                found = A.index(e)
    return found


if __name__ == "__main__":
    _A = [1, 3, 1, 4, 2, 3, 5, 4]
    _X = 5
    print(solution(_A, _X))
