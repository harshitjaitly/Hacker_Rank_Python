# Enter your code here. Read input from STDIN. Print output to STDOUT
N , M = input().split()
N = int(N)
M = int(M)
for i in range(N):
    dash = round((M-(2*i+1)*3)/2)
    if(dash>0) :
        print("-"*dash + ".|."*(2*i+1) + "-"*dash)
    elif(dash<0) :
        dash = dash*-1
        print("-"*dash + ".|."*(2*(N-i)-1) + "-"*dash)
    else :
        dash = round((M-len("WELCOME"))/2)
        print("-"*dash+"WELCOME"+"-"*dash)

## optimum solution

# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
