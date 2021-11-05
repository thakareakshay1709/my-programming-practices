def solution(S):
    n = len(S)
    # edge case and obvious
    if n % 2 != 0:
        return 0
    if n == 0:
        return 1

    brackets = {"(": ")", "{": "}", "[": "]"}
    stack = [None] * n
    size = 0
    for ch in S:
        if ch in brackets:
            stack[size] = ch
            size += 1
        else:
            if size == 0 or brackets[stack[size-1]] != ch:
                return 0
            size -= 1
    return 1 if size == 0 else 0


if __name__ == "__main__":
    _s = "([)()]" # ([)()] # {[()()]}
    print(solution(_s))
