hrizCount = int(input())
roseCount = int(input())
laleCount = int(input())
season = input()
isFairy = input()

hrizPrice = 0
rosePrice = 0
lalePrice = 0

if season == "Spring" or season == "Summer":
    hrizPrice = 2.00 if isFairy == "N" else 2.00 * 1.15
    rosePrice = 4.10 if isFairy == "N" else 4.10 * 1.15
    lalePrice = 2.50 if isFairy == "N" else 2.50 * 1.15

else:
    hrizPrice = 3.75 if isFairy == "N" else 3.75 * 1.15
    rosePrice = 4.50 if isFairy == "N" else 4.50 * 1.15
    lalePrice = 4.15 if isFairy == "N" else 4.15 * 1.15

totalCost = (hrizCount*hrizPrice) + (roseCount*rosePrice) + (laleCount*lalePrice)

if season == "Spring" and laleCount > 7:
    totalCost *= 0.95
if season == "Winter" and roseCount >= 10:
    totalCost *= 0.9
if hrizCount + roseCount + laleCount > 20:
    totalCost *= 0.8

print(f"{totalCost + 2:.2f}")