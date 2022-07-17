circle_of_people = input().split()
step = int(input()) - 1

current_index = step

killed_people = []
person_to_kill = int

while len(circle_of_people) != 0:

    if current_index >= len(circle_of_people):
        while current_index >= len(circle_of_people):
            current_index = current_index - len(circle_of_people)
        killed_people.append(circle_of_people.pop(current_index))
    else:
        killed_people.append(circle_of_people.pop(current_index))

    current_index += step

print(f"[{','.join(killed_people)}]")