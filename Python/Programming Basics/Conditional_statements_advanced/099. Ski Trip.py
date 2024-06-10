days = int(input()) - 1
type = input()
review = input()

price = 0

if type == "room for one person":
    price = days * 18.00
elif type == "apartment":
    if days < 10:
        price = (days * 25.00) * 0.7
    elif 10 <= days <= 15:
        price = (days * 25.00) * 0.65
    else:
        price = (days * 25.00) * 0.5
else:
    if days < 10:
        price = (days * 35.00) * 0.9
    if 10 <= days <= 15:
        price = (days * 35.00) * 0.85
    elif days > 15:
        price = (days * 35.00) * 0.8

if review == "positive":
    price *= 1.25
else:
    price *= 0.9

print(f"{price:.2f}")
