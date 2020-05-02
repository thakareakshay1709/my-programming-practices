
#Creating empty dictionary

phoneBook = {}

totalEntries = int(input("Enter total entries\n"))


for _ in range(0, totalEntries):
	user, telephone = input().split()   ##split function in python uses to accept multiple input from user with some seperator
	phoneBook[user] = telephone

for _ in range(0, totalEntries):
	user = input()
	if user in phoneBook:
		print("{}={}".format(user, phoneBook[user]))
	else:
		print("Not found")




#print(phoneBook)