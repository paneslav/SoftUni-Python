groups = int(input())

total_people = 0

musala_climbers = 0
montblanc_climbers = 0
kiliman_climbers = 0
k2_climbers = 0
everest_climbers = 0

for i in range(0, groups):
    people_in_group = int(input())
    total_people += people_in_group

    if people_in_group <= 5:
        musala_climbers += people_in_group
    elif 6 <= people_in_group <= 12:
        montblanc_climbers += people_in_group
    elif 13 <= people_in_group <= 25:
        kiliman_climbers += people_in_group
    elif 26 <= people_in_group <= 40:
        k2_climbers += people_in_group
    else:
        everest_climbers += people_in_group

print(f"{(musala_climbers/total_people)*100:.2f}%")
print(f"{(montblanc_climbers/total_people)*100:.2f}%")
print(f"{(kiliman_climbers/total_people)*100:.2f}%")
print(f"{(k2_climbers/total_people)*100:.2f}%")
print(f"{(everest_climbers/total_people)*100:.2f}%")