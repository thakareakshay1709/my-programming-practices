class Calculator(object):
    def power(self,number,power):
        if(number < 0 or power < 0):
            raise Exception("n and p should be non-negative")
        else:
            return number**power


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)