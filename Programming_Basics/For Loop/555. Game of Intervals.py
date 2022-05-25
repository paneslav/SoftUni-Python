n = int(input())

result = 0
zero_9 = 0
ten_19 = 0
twenty_29 = 0
thirty_39 = 0
forty_50 = 0
invalid_numbers = 0


for i in range(1, n+1):
    number = int(input())

    if 0 <= number < 10:
        zero_9 += 1
        result += number * 0.2
    elif 10 <= number < 20:
        ten_19 += 1
        result += number * 0.3
    elif 20 <= number < 30:
        twenty_29 += 1
        result += number * 0.4
    elif 30 <= number < 40:
        thirty_39 += 1
        result += 50
    elif 40 <= number <= 50:
        forty_50 += 1
        result += 100
    elif number < 0 or number > 50:
        result /= 2
        invalid_numbers += 1

print(f"{result:.2f}")
print(f"From 0 to 9: {zero_9/n*100:.2f}%")
print(f"From 10 to 19: {ten_19/n*100:.2f}%")
print(f"From 20 to 29: {twenty_29/n*100:.2f}%")
print(f"From 30 to 39: {thirty_39/n*100:.2f}%")
print(f"From 40 to 50: {forty_50/n*100:.2f}%")
print(f"Invalid numbers: {invalid_numbers/n*100:.2f}%")