# Link - https://www.hackerrank.com/challenges/polar-coordinates/problem

# import cmath
# print(*cmath.polar(complex(input())), sep='\n')

# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase
complex_num = complex(input())
print(abs(complex_num) , phase(complex_num) , sep='\n')
