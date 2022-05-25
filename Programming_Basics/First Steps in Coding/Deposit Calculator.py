deposit = float(input())
time = int(input())
lihva = float(input())

sum = deposit + time * ((deposit * (lihva/100)) / 12)

print(sum)