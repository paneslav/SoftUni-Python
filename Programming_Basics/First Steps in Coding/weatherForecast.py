degress = float(input())

if 26.00 <= degress <= 35.00:
    print("Hot")
elif 20.1 <= degress <= 25.9:
    print("Warm")
elif 15.00 <= degress <= 20.00:
    print("Mild")
elif 12.00 <= degress <= 14.9:
    print("Cool")
elif 5.00 <= degress <= 11.9:
    print("Cold")
else:
    print("unknown")