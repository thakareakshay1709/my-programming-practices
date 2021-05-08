import numpy

rows, cols = map(int, input().strip().split())
cols_list = []

for r in range(rows):
    cols_list.append(list(input().strip().split()))

num_arr = numpy.array(cols_list, int)

print(numpy.transpose(num_arr))
print(num_arr.flatten())
