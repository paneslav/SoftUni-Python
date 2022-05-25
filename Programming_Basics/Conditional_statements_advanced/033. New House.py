flowers = input()
quant = int(input())
budget = int(input())

price = 0

if flowers == "Roses":
    price = quant * 5
    if quant > 80:
        price *= 0.9
elif flowers == "Dahlias":
    price = quant * 3.80
    if quant > 90:
        price *= 0.85
elif flowers == "Tulips":
    price = quant * 2.80
    if quant > 80:
        price *= 0.85
elif flowers == "Narcissus":
    price = quant * 3
    if quant < 120:
        price *= 1.15
elif flowers == "Gladiolus":
    price = quant * 2.50
    if quant < 80:
        price *= 1.20

if budget >= price:
    print(f"Hey, you have a great garden with {quant} {flowers} and {abs(budget-price):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget-price):.2f} leva more.")