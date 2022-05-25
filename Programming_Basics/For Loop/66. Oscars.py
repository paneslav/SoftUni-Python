actor_name = input()
academy_points = float(input())
jury_number = int(input())

totalPoints = 0

for i in range(1, jury_number + 1):
    jury = input()
    jury_points = (float(input()) * len(jury)) / 2

    totalPoints += jury_points

    if totalPoints + academy_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {totalPoints+academy_points:.1f}!")
        break

if totalPoints + academy_points < 1250.5:
    print(f"Sorry, {actor_name} you need {abs((totalPoints+academy_points) - 1250.5):.1f} more!")