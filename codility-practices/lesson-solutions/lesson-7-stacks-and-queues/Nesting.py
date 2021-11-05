def solution(S):
    if len(S) == 0:
        return 1
    stack = []
    for a in S:
        if a == '(':
            stack.append(a)
        else:
            if len(stack) == 0:
                return 0
            else:
                if stack[len(stack)-1] != '(':
                    return 0
                else:
                    stack.pop(len(stack)-1)

    if len(stack) == 0:
        return 1
    else:
        return 0