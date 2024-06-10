quantity = int(input())
days = int(input())

total_money_spent = 0
total_spirit = 0

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

for current_day in range(1, days + 1):

    if current_day % 11 == 0:
        quantity += 2

    if current_day % 2 == 0:
        total_money_spent += ornament_set * quantity
        total_spirit += 5

    if current_day % 3 == 0:
        total_money_spent += (tree_skirt + tree_garland) * quantity
        total_spirit += 13

    if current_day % 5 == 0:
        total_money_spent += tree_lights * quantity
        total_spirit += 17

    if current_day % 3 == 0 and current_day % 5 == 0:
        total_spirit += 30

    if current_day % 10 == 0:
        total_spirit -= 20
        total_money_spent += tree_skirt + tree_garland + tree_lights

    if current_day == days and current_day % 10 == 0:
        total_spirit -= 30


print(f"Total cost: {total_money_spent}")
print(f"Total spirit: {total_spirit}")