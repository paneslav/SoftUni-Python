import math

days = int(input())
foodLeft = int(input())
dogFood = float(input())
catFood = float(input())
turtleFood = float(input()) / 1000

totalFood = (dogFood*days) + (catFood*days) + (turtleFood*days)

if foodLeft >= totalFood:
    print(f"{math.floor(abs(totalFood-foodLeft))} kilos of food left.")
else:
    print(f"{math.ceil(abs(totalFood-foodLeft))} more kilos of food are needed.")