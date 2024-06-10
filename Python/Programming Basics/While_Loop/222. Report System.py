sum_needed = int(input())

total_cash = 0
total_card = 0
count_cash = 0
count_card = 0

counter = 0
while True:
    n = input()

    if n == "End":
        break

    price = int(n)

    if counter % 2 == 0:
        if price > 100:
            print(f"Error in transaction!")
        else:
            total_cash += price
            count_cash += 1
            print(f"Product sold!")
    else:
        if price < 10:
            print(f"Error in transaction!")
        else:
            total_card += price
            count_card += 1
            print(f"Product sold!")

    if total_card + total_cash >= sum_needed:
        print(f"Average CS: {total_cash/count_cash:.2f}")
        print(f"Average CC: {total_card/count_card:.2f}")
        break
    counter += 1

if total_card + total_cash < sum_needed:
    print(f"Failed to collect required money for charity.")

