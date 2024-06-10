import math

magnolii = int(input())
zumbuli = int(input())
roses = int(input())
cactus = int(input())
price = float(input())

totalCost = ((magnolii*3.25) + (zumbuli*4) + (roses*3.5) + (cactus*8)) * 0.95

if totalCost >= price:
    print(f"She is left with {math.floor(abs(totalCost-price))} leva.")
else:
    print(f"She will have to borrow {math.ceil(abs(totalCost-price))} leva.")