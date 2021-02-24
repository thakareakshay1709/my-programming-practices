for _ in range(int(input())):

    try:
        a, b = map(int, input().split())
        ans = a // b
        print(ans)
    except Exception as e:
        print(f'Error Code: {e}')