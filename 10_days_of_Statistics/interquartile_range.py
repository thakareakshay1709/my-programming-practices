from statistics import median

n = int(input())
X = list(map(int, input().split()))
freq = list(map(int, input().split()))

# S = []
# count = 0
# for f, x in zip(freq, X):
#     count += f
#     while f > 0:
#         S.append(x)
#         f -= 1
S = []
for i in range(n):
    S += [X[i]] * freq[i]
print(S)
count = sum(freq)
print(count)
sorted_dataset = sorted(S)
mid_point = count // 2
# print(sorted_dataset)
if (count % 2) == 0:
    lower = sorted_dataset[:mid_point]
    upper = sorted_dataset[mid_point:]
else:
    lower = sorted_dataset[:mid_point]
    upper = sorted_dataset[mid_point + 1:]

print(round(median(upper) - median(lower), 1))

# working
# n = int(input())
# data = list(map(int, input().split()))
# freq = list(map(int, input().split()))
# import statistics as st
# s = []
# for i in range(n):
#     s += [data[i]] * freq[i]
# N = sum(freq)
# s.sort()
#
# if n%2 != 0:
#     q1 = st.median(s[:N//2])
#     q3 = st.median(s[N//2+1:])
# else:
#     q1 = st.median(s[:N//2])
#     q3 = st.median(s[N//2:])
#
# ir = round(float(q3-q1), 1)
# print(ir)
