# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
# print(N, X)
marks = []
for i in range(X):
    marks.append(map(float, input().split()))

# print(*marks)
for j in zip(*marks):
    print((sum(j) / len(j)))


