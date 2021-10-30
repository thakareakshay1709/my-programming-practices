import numpy

n,m = map(int, input().split())
list_a = []
list_b = []
for _ in range(int(n)):
    list_a.append(list(input().split()))

for _ in range(int(n)):
    list_b.append(list(input().split()))

num_array_a = numpy.array(list_a, int)
num_array_b = numpy.array(list_b, int)

# print(num_array_a + num_array_b)
# print(num_array_a - num_array_b)
# print(num_array_a * num_array_b)
# print(num_array_a // num_array_b)
# print(num_array_a % num_array_b)
# print(num_array_a ** num_array_b)

print(numpy.add(num_array_a, num_array_b))
print(numpy.subtract(num_array_a, num_array_b))
print(numpy.multiply(num_array_a, num_array_b))
print(numpy.floor_divide(num_array_a, num_array_b))
print(numpy.mod(num_array_a, num_array_b))
print(numpy.power(num_array_a, num_array_b))