# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
string, n = input().split()
perm = [''.join(x) for x in permutations(sorted(string),int(n))]
print(*perm, sep='\n')
