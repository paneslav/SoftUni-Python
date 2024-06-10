total_steps = 0

while total_steps < 10000:
    command = input()

    if command == "Going home":
        home_steps = int(input())
        total_steps += home_steps
        break

    steps_per_walk = int(command)
    total_steps += steps_per_walk

if total_steps >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{abs(total_steps-10000)} steps over the goal!")
else:
    print(f"{abs(total_steps-10000)} more steps to reach goal.")
