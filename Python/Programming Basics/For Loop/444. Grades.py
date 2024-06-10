students_count = int(input())

top_students = 0
between_3_4 = 0
between_4_5 = 0
fail = 0
total = 0

for i in range(1, students_count + 1):
    grade = float(input())

    if grade >= 5:
        top_students += 1
    elif 4 <= grade < 5:
        between_4_5 += 1
    elif 3 <= grade < 4:
        between_3_4 +=1
    else:
        fail += 1

    total += grade

average = total / students_count

print(f"Top students: {top_students/students_count*100:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_5/students_count*100:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_4/students_count*100:.2f}%")
print(f"Fail: {fail/students_count*100:.2f}%")
print(f"Average: {average:.2f}")

