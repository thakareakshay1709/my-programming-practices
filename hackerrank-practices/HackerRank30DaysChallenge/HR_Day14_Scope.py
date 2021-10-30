class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = self.computeDifference()

	# Add your code here
    def computeDifference(self):
        #print(self.__elements)
        return (max(self.__elements) - min(self.__elements))


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)