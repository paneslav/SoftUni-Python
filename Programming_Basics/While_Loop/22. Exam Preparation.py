max_unsati = int(input())

task_name = input()

total_tasks = 0
total_score = 0
unsatisfied = 0
last_task = ""

while task_name != "Enough":
    last_task = task_name
    task_grade = float(input())
    if task_grade <= 4:
        unsatisfied += 1
        if unsatisfied == max_unsati:
            print(f"You need a break, {unsatisfied} poor grades.")
            break

    total_score += task_grade
    total_tasks +=1
    task_name = input()
else:
    print(f"Average score: {total_score/total_tasks:.2f}")
    print(f"Number of problems: {total_tasks}")
    print(f"Last problem: {last_task}")