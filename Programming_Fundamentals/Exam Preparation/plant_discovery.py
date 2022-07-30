def add_new_plants():
    n = int(input())
    for _ in range(n):
        plant_name, plant_rarity = input().split('<->')
        if plant_name in plants_data:
            plants_data[plant_name]['rarity'] = int(plant_rarity)
            continue
        plants_data[plant_name] = {'rarity': int(plant_rarity), 'rating': []}


def rate_plant(plant_name, rating):
    plants_data[plant_name]['rating'].append(rating)


def update_rarity(plant_name, rarity):
    plants_data[plant_name]['rarity'] = rarity


def reset_ratings(plant_name):
    plants_data[plant_name]['rating'].clear()


plants_data = {}
add_new_plants()

while True:
    operation = input().split(': ')

    if operation[0] == 'Exhibition':
        break

    plant_info = operation[1].split(' - ')
    plant_name = plant_info[0]

    if plant_name not in plants_data:
        print('error')
        continue

    if operation[0] == 'Rate':
        rating = int(plant_info[1])
        rate_plant(plant_name, rating)

    if operation[0] == 'Update':
        rarity = int(plant_info[1])
        update_rarity(plant_name, rarity)

    if operation[0] == 'Reset':
        reset_ratings(plant_name)

print(f"Plants for the exhibition:")

for plant in plants_data:
    if len(plants_data[plant]['rating']) > 0:
        rating = sum(plants_data[plant]['rating']) / len(plants_data[plant]['rating'])
    else:
        rating = 0

    print(f"- {plant}; Rarity: {plants_data[plant]['rarity']}; Rating: {rating:.2f}")