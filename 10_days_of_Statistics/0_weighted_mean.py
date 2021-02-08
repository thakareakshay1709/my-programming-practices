n, x, w = int(input()), list(map(int, input().split())), list(map(int, input().split()))

numerator = 0
denominator = 0
for i in range(n):
    numerator += x[i] * w[i]
    denominator += w[i]

print(round(numerator / denominator, 1))