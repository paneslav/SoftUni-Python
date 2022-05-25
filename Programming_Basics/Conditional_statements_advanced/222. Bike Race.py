juniors = int(input())
seniors = int(input())
typeOfRoad = input()

totalSum = 0
juniorsTicket = 0
seniorsTicket = 0

if typeOfRoad == "trail":
    juniorsTicket = 5.50
    seniorsTicket = 7
elif typeOfRoad == "cross-country":
    juniorsTicket = 8 if (juniors+seniors) < 50 else 8 * 0.75
    seniorsTicket = 9.50 if (juniors+seniors) < 50 else 9.50 * 0.75
elif typeOfRoad == "downhill":
    juniorsTicket = 12.25
    seniorsTicket = 13.75
else:
    juniorsTicket = 20
    seniorsTicket = 21.50

totalSum = ((juniors*juniorsTicket) + (seniorsTicket*seniors)) * 0.95

print(f"{totalSum:.2f}")