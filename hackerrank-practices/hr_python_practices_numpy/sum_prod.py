import numpy

n, m = map(int, input().split())

rows_l = []

for _ in range(n):
    rows_l.append(list(input().split()))

num_array = numpy.array(rows_l, int)
print(numpy.prod(numpy.sum(num_array, axis=0)))
