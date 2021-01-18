import numpy

inp = [float(x) for x in input().split()]
value = float(input())
print(numpy.polyval(inp, value))
