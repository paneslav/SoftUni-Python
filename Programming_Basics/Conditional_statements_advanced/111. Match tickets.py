budget = float(input())
category = input()
people = int(input())

tripCost = 0
ticketPrice = 0

if 1 <= people <= 4:
    tripCost = budget * 0.75
elif 5 <= people <= 9:
    tripCost = budget * 0.6
elif 10 <= people <= 24:
    tripCost = budget * 0.5
elif 25 <= people <= 49:
    tripCost = budget * 0.4
else:
    tripCost = budget * 0.25

if category == "VIP":
    ticketPrice = 499.99
else:
    ticketPrice = 249.99

totalCost = (people*ticketPrice) + tripCost

if budget >= totalCost:
    print(f"Yes! You have {abs(totalCost-budget):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(totalCost-budget):.2f} leva.")
