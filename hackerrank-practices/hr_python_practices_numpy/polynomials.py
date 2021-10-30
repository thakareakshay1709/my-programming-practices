import numpy

num_coef = numpy.array(input().split(), float)
print(numpy.polyval(num_coef, int(input())))