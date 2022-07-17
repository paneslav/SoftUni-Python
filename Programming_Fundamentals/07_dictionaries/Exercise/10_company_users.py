company_employees = {}

while True:
    command = input().split(' -> ')
    if command[0] == 'End':
        break

    company = command[0]
    employee_id = command[1]

    if company not in company_employees:
        company_employees[company] = []
    if employee_id not in company_employees[company]:
        company_employees[company].append(employee_id)

for company in company_employees:
    data_to_print = [f'-- {name}' for name in company_employees[company]]
    print(f"{company}")
    print('\n'.join(data_to_print))
