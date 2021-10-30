def solution(N):
    _bin = bin(N)[2:].strip('0').split('1')
    return len(max(_bin))


if __name__ == "__main__":
    print(solution(1041))
