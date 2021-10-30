import numpy

n = int(input())
a_list = []
b_list = []
for _ in range(n):
    a_list.append(input().split())
for _ in range(n):
    b_list.append(input().split())

a_array = numpy.array(a_list, int)
b_array = numpy.array(b_list, int)

print(numpy.dot(a_array, b_array))