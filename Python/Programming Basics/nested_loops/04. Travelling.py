destination = input()

saved_money = 0

while destination != "End":
    budget = float(input())

    while budget > saved_money:
        money = float(input())
        saved_money += money

    print(f"Going to {destination}!")
    saved_money = 0
    destination = input()

