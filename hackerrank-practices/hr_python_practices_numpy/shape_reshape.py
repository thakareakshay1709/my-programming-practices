import numpy

li = input().split(' ')
n_array = numpy.array(li, int)
print(n_array.reshape(3, 3))
