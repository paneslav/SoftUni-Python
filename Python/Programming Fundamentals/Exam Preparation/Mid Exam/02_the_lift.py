people_waiting = int(input())
lift_state = list(map(int, input().split()))
breakCycle = False

for index in range(len(lift_state)):

    if breakCycle:
        break

    while lift_state[index] != 4:
        lift_state[index] += 1
        people_waiting -= 1

        if people_waiting == 0:
            breakCycle = True
            break

if lift_state[-1] < 4:
    print("The lift has empty spots!")
elif lift_state[-1] == 4 and people_waiting !=0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")

print(*lift_state, sep=' ')



