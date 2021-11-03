def solution(A):
    count_zero = 0  # track of zeros
    count_all = 0  # track of pairs

    for element in A:
        if element == 0:
            count_zero += 1
        else:
            count_all += count_zero

    if count_all > 1000000000:
        return -1
    return count_all


if __name__ == "__main__":
    _A = [0, 1, 0, 1, 1]
    print(solution(_A))

# explanation
"""
You need to count number of cars passings. Cars are positioned on the road as input says and start driving into either one of directions. When car drives, we can easily see that it will drive by cars moving in the opposite direction, but only if they were in front of it. Essentially that can be formulated as:

Imagine array 0..N

Take element X (iterate from 0 to Nth element)

If value of element X is 0 then count how many 1 elements it has on the right

If value of element X is 1 then count how many 0 elements it has on left

Repeat for next X

Sum up and divide by 2 (cos it takes 2 cars to pass each other), that's the answer.

In case with 0 1 0 1 1 we have 3+1+2+2+2 = 10. Divide by 2 = 5 passings.

We don't count pair 2-1 because 2nd car is driving to the East and never passes the 1st car that is driving away from it to the West.
"""