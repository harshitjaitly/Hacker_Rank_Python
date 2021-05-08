#Link -  https://www.hackerrank.com/challenges/no-idea/forum

# Enter your code here. Read input from STDIN. Print output to STDOUT
import time
n, m = input().split()
array = input().split()
set_A = set(input().split())
set_B = set(input().split())
# happiness = 0
# for each_char in array :
#     if(each_char in set_A) :
#         happiness += 1
#         continue
#     if(each_char in set_B) :
#         happiness += -1
#         continue
# print(happiness)

print(sum([(i in set_A) - (i in set_B) for i in array]))
