months = int(input())

water = 0
internet = 0
others = 0
total_electricity = 0
total_cost = 0
total_others = 0

for i in range(1, months +1):
    electricity = float(input())

    total_electricity += electricity
    water += 20
    internet += 15
    others = (electricity + 20 + 15) * 1.20
    total_others += others

total_cost = total_electricity + water + internet + total_others

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {total_cost/months:.2f} lv")