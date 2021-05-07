# Link - https://www.hackerrank.com/challenges/find-angle/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
side_AB = int(input())
side_BC = int(input())

# The formed triangle is a isosceles triangle , therefore angle same as angle C
theta = round(math.degrees(math.atan(side_AB/side_BC)))
print(theta,chr(176),sep="")
