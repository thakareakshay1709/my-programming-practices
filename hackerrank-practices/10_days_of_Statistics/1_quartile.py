from statistics import median
n, x = int(input()), list(map(int, input().split()))

sorted_x = sorted(x)
length = len(sorted_x)
mid_point = int(length/2)

if (length % 2) == 0:
    lower = sorted_x[:mid_point]
    upper = sorted_x[mid_point:]
else:
    lower = sorted_x[:mid_point]
    upper = sorted_x[mid_point+1:]


print(int(median(lower)))
print(int(median(sorted_x)))
print(int(median(upper)))
