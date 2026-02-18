# from math import pi
import math
figure = input()

if figure == "square":
    side = float(input())
    print(f"{math.pow(side, 2):.3f}")
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    print(f"{side_a * side_b:.3f}")
elif figure == "circle":
    r = float(input())
    print(f"{math.pow(r, 2) * math.pi:.3f}")
elif figure == "triangle":
    h_b = float(input())
    b = float(input())
    print(f"{h_b * b / 2:.3f}")