#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    gmail_regex = re.compile("^[a-z\.]+@gmail.com$")
    gmail_accounts = dict()
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        #pattern="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
        if gmail_regex.match(emailID):
            gmail_accounts[emailID] = firstName
            #print(firstName,emailID)
    sorted_names = sorted(gmail_accounts.values())
    print(*sorted_names, sep="\n")
