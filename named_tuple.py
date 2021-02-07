# link - https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N , entry = int(input()) , namedtuple("Entry", input())
marks = [int(entry(*input().split()).MARKS) for _ in range(N)]
print(sum(marks)/len(marks))
