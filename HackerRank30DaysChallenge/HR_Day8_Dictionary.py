
#Creating empty dictionary

# phoneBook = {}
#
# totalEntries = int(input("Enter total entries\n"))
#
#
# for _ in range(0, totalEntries):
# 	user, telephone = input().split()   ##split function in python uses to accept multiple input from user with some seperator
# 	phoneBook[user] = telephone
#
# for _ in range(0, totalEntries):
# 	user = input()
# 	if user in phoneBook:
#
# 		print(user + "=" + phoneBook[user])
# 	else:
# 		print("Not found")

import sys

n = int(input())
phone_book = {}

for _ in range(n):
	element = list(map(str, input().rstrip().split()))
	phone_book[element[0]] =(element[1])
#print(phone_book)


s = input()
while(s):
	if phone_book.__contains__(s):
		print (s+"="+phone_book[s])
	else:
		print('Not found')
	s = sys.stdin.readline().strip()
