#Accept input from user
nTestCases = int(input())

#Function to check primality of number
def checkPrimality(number):
    no = True
    sqrt = int(number**0.5)
    for i in range(2,sqrt+1):
        #print(i)
        if i !=1 and i!=number and number%i == 0:
            no = False
            break;
    if no:
        print('Prime')
    else:
        print('Not prime')



#Accept numbers till nTestCases
for i in range(nTestCases):
    number = int(input())
    #print(number)
    if number == 1:
        print('Not prime')
    else:
        checkPrimality(number)