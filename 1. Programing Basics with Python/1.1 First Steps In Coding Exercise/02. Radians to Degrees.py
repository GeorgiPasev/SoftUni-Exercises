# input float radians converted to degrees
# formula degree = radian * 180/π

import math # import the whole math library (with this you have to use math.pi
# instead of just pi)
from math import pi # importing just the function pi from the math library

radians = float(input())
degrees = radians * 180 / pi
print(degrees)