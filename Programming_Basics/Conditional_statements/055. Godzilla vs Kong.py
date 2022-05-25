filmBudget = float(input())
statistCount = int(input())
priceForStatist = float(input())

decor = filmBudget*0.1
cloathBudget = statistCount * priceForStatist

if statistCount > 150:
    cloathBudget *= 0.9

moneyNeeded = decor + cloathBudget

if moneyNeeded > filmBudget:
    print("Not enough money!")
    print(f"Wingard needs {moneyNeeded-filmBudget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {filmBudget-moneyNeeded:.2f} leva left.")



