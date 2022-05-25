lenght = float(input()) * 100
widht = float(input()) * 100

deskPerRow = (widht-100) // 70
rows = lenght // 120

totalDesks = deskPerRow*rows-3

print(int(totalDesks))