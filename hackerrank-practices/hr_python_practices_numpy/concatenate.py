import numpy

n, m, p = map(int, input().strip().split())
# print(n,m,p)
arr_list = []

for _ in range(int(n + m)):
    arr_list.append(list(input().split()))
# print(arr_list)
num_arr = numpy.array(arr_list, int)
print(num_arr, sep='\n')
