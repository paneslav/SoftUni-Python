days = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for i in range(1, days + 1):

    if i % 3 == 0 and (untreated_patients > treated_patients):
        doctors += 1

    patients = int(input())

    for y in range(1, doctors + 1):
        if patients == 0:
            break

        treated_patients += 1
        patients -= 1

    untreated_patients += patients

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
