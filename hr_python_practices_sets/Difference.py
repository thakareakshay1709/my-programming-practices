# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
eng_list = list(map(int, input().split()))
french = int(input())
frn_list = list(map(int, input().split()))
diff = set(eng_list).difference(set(frn_list))
print(len(diff))