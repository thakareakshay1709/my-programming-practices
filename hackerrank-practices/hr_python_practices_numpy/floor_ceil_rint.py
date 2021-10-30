import numpy
numpy.set_printoptions(legacy='1.13')
# l_ = list(input().split())
num_arr = numpy.array(input().split(), float)

print(numpy.floor(num_arr))
print(numpy.ceil(num_arr))
print(numpy.rint(num_arr))