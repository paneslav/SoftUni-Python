def avg_grade(value):
    return sum(value) / len(value)


number_of_students = int(input())

students = {}

for i in range(number_of_students):
    student, grade = input().split()

    if student not in students:
        students[student] = []

    students[student].append(float(grade))


for key, value in students.items():
    average_grade = avg_grade(value)
    print(f"{key} -> {' '.join(f'{grade:.2f}' for grade in value)} (avg: {average_grade:.2f})")