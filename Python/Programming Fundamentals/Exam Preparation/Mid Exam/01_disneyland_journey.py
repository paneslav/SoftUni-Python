journey_cost = float(input())
months = int(input())

month_counter = 1

budget = 0

for i in range(months):
    if month_counter > 1 and month_counter % 2 != 0:
        budget -= budget * 0.16

    if month_counter % 4 == 0:
        budget += budget * 0.25

    budget += journey_cost * 0.25

    month_counter += 1


if budget >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {budget - journey_cost:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {journey_cost - budget:.2f}lv. more.")