class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    # Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    def __init__(self, firstName, lastName, id, scores):
        super().__init__(firstName, lastName, id)
        self.score = scores




# Write your constructor here


#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here
    def calculate(self):
        # count = 0
        # total = 0
        # for i in self.score:
        #     print(int(i))
        #     count += 1
        #     total = total + int(i)
        # mean = total/count

        mean = float(sum(self.score) / len(self.score))
        mean = round(mean)
        print(mean)

        if mean < 40:
            return 'T'
        elif mean >= 90 and mean <=100:
            return 'O'
        elif mean >= 80 and mean < 90:
            return 'E'
        elif mean >= 70 and mean < 80:
            return 'A'
        elif mean >= 55 and mean < 70:
            return 'P'
        elif mean >= 40 and mean < 55:
            return 'D'
        else:
            return ""


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())