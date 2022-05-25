courses = int(input())

total_weight = 0
microbus = 0
truck = 0
train = 0

microbus_price = 200
truck_price = 175
train_price = 120

for i in range(1, courses +1):
    tons = int(input())

    total_weight += tons

    if tons <= 3:
        microbus += tons
    elif 4 <= tons <= 11:
        truck += tons
    else:
        train += tons

total_price = (microbus_price*microbus) + (truck_price*truck) + (train*train_price)
average_price = total_price/total_weight

print(f"{average_price:.2f}")
print(f"{microbus/total_weight*100:.2f}%")
print(f"{truck/total_weight*100:.2f}%")
print(f"{train/total_weight*100:.2f}%")