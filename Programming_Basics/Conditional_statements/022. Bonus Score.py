points = int(input())
bonus = 0

if points % 2 == 0:
    if points <= 100:
        print(6)
        print(points + 6)
    elif 100 < points < 1000:
        print(points * 0.2 + 1)
        print(points +(points*0.2+1))
    elif points > 1000:
        print(points * 0.1 + 1)
        print(points + (points*0.1+1))
elif points % 5 == 0:
    if points <= 100:
        print(7)
        print(points + 7)
    elif 100 < points < 1000:
        print(points * 0.2 + 2)
        print(points +(points*0.2 + 2))
    elif points > 1000:
        print(points * 0.1 + 2)
        print(points + (points*0.1+2))
else:
    if points <= 100:
        print(5)
        print(points + 5)
    elif 100 < points < 1000:
        print(points * 0.2)
        print(points +(points*0.2))
    elif points > 1000:
        print(points * 0.1)
        print(points + (points*0.1))