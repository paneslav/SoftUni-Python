current_year = int(input())

isDistinct = False

while not isDistinct:

    year_set = set()
    current_year += 1

    for i in range(len(str(current_year))):
        year_set.add(str(current_year)[i])

    isDistinct = len(year_set) == len(str(current_year))

print(current_year)