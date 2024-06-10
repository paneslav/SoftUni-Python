name = input()
counter = 0
exclusion = 0
total = 0

while True:
    grade = float(input())

    if grade >= 4:
        counter += 1
        total += grade

    if counter == 12:
        print(f"{name} graduated. Average grade: {total/12:.2f}")
        break

    if grade < 4:
        exclusion += 1
        if exclusion == 2:
            print(f"{name} has been excluded at {counter+1} grade")
            break
