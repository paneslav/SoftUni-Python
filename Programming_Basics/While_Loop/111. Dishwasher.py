bottles = int(input())
total_ml = bottles * 750

counter = 1
total_dishes = 0
total_pots = 0
while True:
    n = input()

    if n == "End":
        print(f"Detergent was enough!\n{total_dishes} dishes and {total_pots} pots were washed.\nLeftover detergent {total_ml} ml.")
        break

    dishes = int(n)

    if counter % 3 == 0:
        total_ml = total_ml - (dishes*15)
        total_pots += dishes
    else:
        total_ml = total_ml - (dishes*5)
        total_dishes += dishes

    if total_ml < 0:
        print(f"Not enough detergent, {abs(total_ml)} ml. more necessary!")
        break

    counter += 1
