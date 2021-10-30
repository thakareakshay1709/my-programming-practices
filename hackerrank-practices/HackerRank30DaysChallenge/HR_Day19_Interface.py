class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        #print(n)
        total = 0
        for i in range(1,n+1):
            #print(i)
            if n % i == 0:
                total = total + i
        #print(total)
        return total



n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)