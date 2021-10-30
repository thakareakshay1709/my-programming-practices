n,m = input().split()
gen_array,set_A,set_B = list(map(int, input().split())),set(map(int, input().split())),set(map(int, input().split()))

happiness = 0
for each in gen_array:
    if set_A.__contains__(each):
        happiness += 1
    elif set_B.__contains__(each):
        happiness -= 1

print(happiness)