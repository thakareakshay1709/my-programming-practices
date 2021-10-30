if __name__ == '__main__':
    s = input()
    
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False

    for i in s:
        alnum = i.isalnum()
        if alnum:
            break
    for i in s:
        alpha = i.isalpha()
        if alpha:
            break
    for i in s:
        digit = i.isdigit()
        if digit:
            break

    for i in s:
        lower = i.islower()
        if lower:
            break
    for i in s:
        upper = i.isupper()
        if upper:
            break

    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)