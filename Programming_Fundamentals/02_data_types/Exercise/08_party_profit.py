import math

people = int(input())
days = int(input())

total_money = 0
money_per_person = 0


for i in range(1, days + 1):

    if i % 10 == 0:
        people -= 2
    if i % 15 == 0:
        people += 5

    food_cost = 2 * people

    total_money += 50 - food_cost

    if i % 3 == 0:
        total_money -= 3 * people
    if i % 5 == 0:
        total_money += 20 * people
        if i % 3 == 0:
            total_money -= 2 * people

money_per_person = math.floor(total_money / people)

print(f"{people} companions received {money_per_person} coins each.")