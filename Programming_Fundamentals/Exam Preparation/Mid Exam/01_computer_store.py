price_without_taxes = 0
taxes = 0

while True:

    price = input()
    if price == 'special' or price == 'regular':
        break
    price = float(price)
    if price < 0:
        print(f'Invalid price!')
        continue
    price_without_taxes += price
    taxes += price * 0.2

total_money = price_without_taxes + taxes

if total_money == 0:
    print(f"Invalid order!")
    exit()
if price == 'special':
    total_money *= 0.9

print(f"Congratulations you've just bought a new computer!")
print(f"Price without taxes: {price_without_taxes:.2f}$")
print(f"Taxes: {taxes:.2f}$")
print(f"-----------")
print(f"Total price: {total_money:.2f}$")