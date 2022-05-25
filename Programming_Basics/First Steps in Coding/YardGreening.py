import math

cubicMeters = float(input())

discount = (cubicMeters * 7.61) * 0.18
finalPrice = (cubicMeters * 7.61) - discount

print(f"The final price is: {finalPrice} lv.")
print(f"The discount is: {discount} lv.")