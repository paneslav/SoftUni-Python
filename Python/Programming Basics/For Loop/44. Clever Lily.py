age = int(input())
laundry_machine_cost = float(input())
toyPrice = int(input())

toysCount = 0
moneyCount = 0

moneyCounter = 10

for i in range(1, age + 1):
    if i % 2 == 0:
        moneyCount += moneyCounter - 1
        moneyCounter += 10
    else:
        toysCount += 1

totalMoney = (toyPrice*toysCount) + moneyCount

if totalMoney >= laundry_machine_cost:
    print(f"Yes! {abs(totalMoney-laundry_machine_cost):.2f}")
else:
    print(f"No! {abs(totalMoney-laundry_machine_cost):.2f}")