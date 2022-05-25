import math

size = int(input())
grapePerSq = float(input())
wineNeeded = int(input())
workers = int(input())

totalWine = (size*grapePerSq*0.4) / 2.5

if wineNeeded <= totalWine:
    print(f"Good harvest this year! Total wine: {math.floor(totalWine)} liters.")
    print(f"{math.ceil(totalWine-wineNeeded)} liters left -> {math.ceil((totalWine-wineNeeded)/workers)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(wineNeeded-totalWine)} liters wine needed.")