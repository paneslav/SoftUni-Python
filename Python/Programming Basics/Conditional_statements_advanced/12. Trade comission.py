city = input()
volume = float(input())

if city == "Sofia":
    if 0 <= volume <= 500:
        print(f"{volume*0.05:.2f}")
    elif 500 < volume <= 1000:
        print(f"{volume*0.07:.2f}")
    elif 1000 < volume <= 10000:
        print(f"{volume*0.08:.2f}")
    elif volume > 10000:
        print(f"{volume*0.12:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= volume <= 500:
        print(f"{volume*0.045:.2f}")
    elif 500 < volume <= 1000:
        print(f"{volume*0.075:.2f}")
    elif 1000 < volume <= 10000:
        print(f"{volume*0.1:.2f}")
    elif volume > 10000:
        print(f"{volume*0.13:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= volume <= 500:
        print(f"{volume*0.055:.2f}")
    elif 500 < volume <= 1000:
        print(f"{volume*0.08:.2f}")
    elif 1000 < volume <= 10000:
        print(f"{volume*0.12:.2f}")
    elif volume > 10000:
        print(f"{volume*0.145:.2f}")
    else:
        print("error")
else:
    print("error")