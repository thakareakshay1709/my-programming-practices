import numpy

n, m = map(int, input().split())
array_lst = []
for _ in range(n):
    array_lst.append(input().split())

num_arr = numpy.array(array_lst, int)

print(numpy.max(numpy.min(num_arr, axis=1)))

# np.max(
#     np.min(
#         np.array([input().split() for _ in range(int(input().split()[0]))],int),axis=1
#     )
# )
