money = float(input())
death = int(input())

age = 18

for i in range(1800, death + 1):
    if i % 2 == 0:
        money -= 12_000
    else:
        money = money - (12000 + (50 * age))

    age += 1

if money < 0:
    print(f"He will need {abs(money):.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {abs(money):.2f} dollars left.")
