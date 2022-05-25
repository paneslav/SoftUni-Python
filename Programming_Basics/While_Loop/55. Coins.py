import math

change = float(input()) * 100
count = 0

while change > 0:
    if change >= 200:
        change -= 200
        count += 1
        round(change)
    elif 100 <= change < 200:
        change -= 100
        count += 1
    elif 50 <= change < 100:
        change -= 50
        count += 1
    elif 20 <= change < 50:
        change -= 20
        count += 1
    elif 10 <= change < 20:
        change -= 10
        count += 1
    elif 5 <= change < 10:
        change -= 5
        count += 1
    elif 2 <= change < 5:
        change -= 2
        count += 1
    elif 1 <= change < 2:
        change -= 1
        count += 1

    if change < 0.01:
        print(count)
        break
else:
    print(count)
