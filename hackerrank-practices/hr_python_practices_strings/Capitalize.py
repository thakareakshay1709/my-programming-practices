def solve(s):
    for each in s.split():
        s = s.replace(each, each.capitalize())
    return s


s = input()
print(solve(s))
