n = int(input())

student_grades = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

data_to_print = [f'{name} -> {sum(student_grades[name]) / len(student_grades[name]):.2f}' for name in student_grades \
                 if sum(student_grades[name]) / len(student_grades[name]) >= 4.50]

print('\n'.join(data_to_print))