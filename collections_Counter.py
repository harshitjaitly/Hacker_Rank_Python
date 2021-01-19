#Link - https://www.hackerrank.com/challenges/collections-counter/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
shoes = Counter(list(map(int, input().split())))

money = 0
for i in range(int(input())):

    size, price = list(map(int,input().split()))
    if(shoes[size] > 0):
        money += price
        shoes[size] -= 1
    else:
        continue
print(money)
