degrees = int(input())
time = input()

if time == "Morning":
    if 10 <= degrees <=18:
        print(f"It's {degrees} degrees, get your Sweatshirt and Sneakers.")
    elif 18 < degrees <= 24:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
elif time == "Afternoon":
    if 10 <= degrees <=18:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif 18 < degrees <= 24:
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your Swim Suit and Barefoot.")
elif time == "Evening":
    if 10 <= degrees <=18:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif 18 < degrees <= 24:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")