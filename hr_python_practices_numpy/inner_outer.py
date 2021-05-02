import numpy

num_arr_a = numpy.array(input().split(), int)
num_arr_b = numpy.array(input().split(), int)

print(numpy.inner(num_arr_a, num_arr_b))
print(numpy.outer(num_arr_a, num_arr_b))