month = input()
days = int(input())

studioPrice = 0
apartmentPrice = 0

if month == "May" or month == "October":
    studioPrice = days * 50
    apartmentPrice = days * 65
    if 7 < days <= 14:
        studioPrice *= 0.95
    elif days > 14:
        studioPrice *= 0.7
        apartmentPrice *= 0.9
elif month == "June" or month == "September":
    studioPrice = days * 75.20
    apartmentPrice = days * 68.70
    if days > 14:
        studioPrice *= 0.8
        apartmentPrice *= 0.9
elif month == "July" or month == "August":
    studioPrice = days * 76
    apartmentPrice = days * 77
    if days > 14:
        apartmentPrice *= 0.9

print(f"Apartment: {apartmentPrice:.2f} lv.\nStudio: {studioPrice:.2f} lv.")