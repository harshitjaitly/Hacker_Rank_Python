#Link - https://www.hackerrank.com/challenges/symmetric-difference/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
size_1 = input()
set_1 = set(input().split())
size_2 = input()
set_2 = set(input().split())
sym_diff = sorted(map(int, set_1.union(set_2).difference(set_1.intersection(set_2))))
print(*sym_diff, sep="\n")

# Better Solution

# set_1,set_2 = [set(input().split()) for _ in range(4)][1::2]
# #Starts from 2nd element of list thereby choosing every alternate i.e. both the sets

# print(*sorted(set_1^set_2 , key=int), sep="\n")
