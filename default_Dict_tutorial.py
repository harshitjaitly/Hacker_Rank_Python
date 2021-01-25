# link - https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split())
A = defaultdict(list)
for i in range(n) :
    A[input()].append(i+1)

for j in range(m) :
    print(*A[input()] or [-1])
