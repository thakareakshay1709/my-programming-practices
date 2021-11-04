def soluton(A): # solution gives 100
    print(A)
    min_sum = (A[0] + A[1])/2
    min_index = 0

    for i in range(len(A)-1):
        tot = (A[i] + A[i+1])
        avg = tot/2
        if avg < min_sum:
            min_sum = avg
            min_index = i
        if i+2 < len(A):
            tot += A[i+2]
            avg = tot/3
            if avg < min_sum:
                min_sum = avg
                min_index = i
    return min_index


if __name__ == "__main__":
    _a = [4, 2, 2, 5, 1, 5, 8]
    print(soluton(_a))
