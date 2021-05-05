import numpy
# numpy.set_printoptions(legacy='1.13')
n,m = map(int, input().split())
arr_list = []
for _ in range(n):
    arr_list.append(input().split())
num_arr = numpy.array(arr_list, float)

print(numpy.mean(num_arr, axis=1))
print(numpy.var(num_arr, axis=0))
print(numpy.around(numpy.std(num_arr), decimals=11))

