import numpy

dims = list(input().split())

tup_dim = (tuple(int(i) for i in dims))

print(numpy.zeros(tup_dim, int))
print(numpy.ones(tup_dim, int))