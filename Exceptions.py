# link - https://www.hackerrank.com/challenges/exceptions/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for _ in range(n) :
    a,b = input().split()
    try :
        print(int(a) // int(b))
    except Exception as e :
        print ("Error Code:", e)
