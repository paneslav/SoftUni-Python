# students_information = {}
#
# while True:
#     command = input().split(':')
#     if len(command) < 3:
#         command = command[0].split('_')
#         command = ' '.join(command)
#         for item in students_information[command]:
#             print(f"{item} - {students_information[command][item]}")
#         break
#
#     name = command[0]
#     student_id = command[1]
#     course = command[2]
#
#     if course not in students_information:
#         students_information[course] = {}
#     students_information[course][name] = student_id

student_information = input()

student_dic = dict()

while not student_dic.get(student_information):
    student_information = student_information.split(":")
    name_student = student_information[0]
    id_student = student_information[1]
    couse_student = student_information[-1]
    if couse_student not in student_dic:
        student_dic[couse_student] = {}
    student_dic[couse_student][name_student] = id_student
    student_information = input()
    student_information = student_information.replace("_", " ")

for key, value in student_dic[student_information].items():
    print(f"{key} - {value}")