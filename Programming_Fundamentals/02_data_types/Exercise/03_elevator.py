people = int(input())
capacity = int(input())

total_courses = (people//capacity)

if people % capacity > 0:
    total_courses += 1

print(total_courses)