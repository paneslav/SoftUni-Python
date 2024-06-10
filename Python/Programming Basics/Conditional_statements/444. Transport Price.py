km = int(input())
timeOfDay = input()

if km < 20:
    if timeOfDay == "day":
        print(f"{km*0.79 + 0.70:.2f}")
    else:
        print(f"{km*0.9 + 0.70:.2f}")
elif 20 <= km < 100:
    print(f"{km*0.09:.2f}")
elif km >= 100:
    print(f"{km*0.06:.2f}")
    