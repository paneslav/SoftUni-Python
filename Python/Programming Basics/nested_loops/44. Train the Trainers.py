number_of_grades = int(input())

project_name = input()
project_total = 0
project_avg = 0
total_avg = 0
sum = 0
project_num = 0

while project_name != "Finish":
    project_num += 1
    for i in range(1, number_of_grades + 1):
        grade = float(input())
        sum += grade

    print(f"{project_name} - {sum/number_of_grades:.2f}.")
    total_avg += sum/number_of_grades

    project_name = input()
    sum = 0

print(f"Student's final assessment is {total_avg/project_num:.2f}.")