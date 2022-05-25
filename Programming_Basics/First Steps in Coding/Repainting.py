nailon = (int(input()) + 2) * 1.50
paint = int(input()) * 14.50
razreditel = int(input()) * 5
hours = int(input())

torbichki = 0.40

sum = nailon + (paint + (paint*0.10)) + razreditel + torbichki
sumHour = (sum * 0.30) * hours

totalSum = sum + sumHour
print(totalSum)
