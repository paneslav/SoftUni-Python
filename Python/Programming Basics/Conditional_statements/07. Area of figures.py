import math

type = input()

if type == "square":
    area = float(input())**2
    print(f"{area:.3f}")
elif type == "rectangle":
    area = float(input()) * float(input())
    print(f"{area:.3f}")
elif type == "circle":
    area = math.pi * (float(input())**2)
    print(f"{area:.3f}")
elif type == "triangle":
    area = float(input()) * float(input()) / 2
    print(f"{area:.3f}")