needed_money = float(input())
current_money = float(input())

days_passed = 0
spends = 0
last_action = ""
while current_money < needed_money:
    days_passed += 1
    action = input()
    last_action = action
    sum = float(input())

    if action == "spend":
        spends += 1
        if sum > current_money:
            current_money = 0
        else:
            current_money -= sum
        if spends == 5:
            print(f"You can't save the money.\n{days_passed}")
            break
    elif action == "save":
        current_money += sum
        spends = 0

else:
    print(f"You saved the money for {days_passed} days.")