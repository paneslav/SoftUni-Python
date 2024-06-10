season = input()
km = float(input())

pricePerKm = 0

if season == "Spring" or season == "Autumn":
    if km <= 5000:
        pricePerKm = 0.75
    elif 5000 < km <= 10000:
        pricePerKm = 0.95
elif season == "Summer":
    if km <= 5000:
        pricePerKm = 0.9
    elif 5000 < km <= 10000:
        pricePerKm = 1.10
else:
    if km <= 5000:
        pricePerKm = 1.05
    elif 5000 < km <= 10000:
        pricePerKm = 1.25

if 10000 < km <= 20000:
    pricePerKm = 1.45

payment = ((km*pricePerKm) * 4) * 0.9

print(f"{payment:.2f}")