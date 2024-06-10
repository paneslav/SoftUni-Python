employees_score = list(map(int, input().split()))
factor = int(input())

half_employees = len(employees_score) // 2

multiplied_employees_score = [x * factor for x in employees_score]
average = sum(multiplied_employees_score) // len(employees_score)

happy_people_list = [x for x in multiplied_employees_score if x > average]

if len(happy_people_list) < half_employees:
    print(f"Score: {len(happy_people_list)}/{len(employees_score)}. Employees are not happy!")
else:
    print(f"Score: {len(happy_people_list)}/{len(employees_score)}. Employees are happy!")
