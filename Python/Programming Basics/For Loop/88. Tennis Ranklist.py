tournaments_attended = int(input())
entry_points = int(input())

total_points = 0
tournaments_won = 0

for i in range(0, tournaments_attended):
    outcome = input()

    if outcome == "W":
        total_points += 2000
        tournaments_won += 1
    elif outcome == "F":
        total_points += 1200
    else:
        total_points += 720


print(f"Final points: {entry_points+total_points}")
print(f"Average points: {total_points//tournaments_attended}")
print(f"{tournaments_won/tournaments_attended*100:.2f}%")