import sys


S = input().strip()

#Trying a condition without exception
try:
    S = int(S)
    print(S)
except(ValueError): #After exception print below
    print('Bad String')

