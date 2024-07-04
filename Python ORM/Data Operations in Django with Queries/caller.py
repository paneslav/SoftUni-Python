import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import *
from decimal import Decimal


# Create queries within functions

def create_pet(name, species):
    pet = Pet(name=name, species=species)
    pet.save()

    return f'{pet.name} is a very cute {pet.species}!'


# 2

def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(name=name, origin=origin, age=age, description=description, is_magical=is_magical)

    return f'The artifact {name} is {age} years old!'


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


# 3

def show_all_locations():
    result = []
    locations = Location.objects.all().order_by('-id')

    for location in locations:
        result.append(f'{location.name} has a population of {location.population}!')

    return '\n'.join(result)


def new_capital():
    first_location = Location.objects.first()

    first_location.is_capital = True
    first_location.save()


def get_capitals():
    return Location.objects.all().filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.first().delete()


# 4


def apply_discount():
    def find_discount_percentage(number):
        return sum(int(digit) for digit in str(number))

    all_cars = Car.objects.all()

    for car in all_cars:
        discount = Decimal(find_discount_percentage(car.year)) / 100
        car.price_with_discount = car.price - (car.price * discount)

    Car.objects.bulk_update(all_cars, ['price_with_discount'])


def get_recent_cars():
    return Car.objects.all().filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


# 5

def show_unfinished_tasks():
    result = []
    unfinished_tasks = Task.objects.all().filter(is_finished=False)

    for task in unfinished_tasks:
        result.append(f'Task - {task.title} needs to be done until {task.due_date}!')

    return '\n'.join(result)


def complete_odd_tasks():
    all_tasks = Task.objects.all()
    odd_tasks = [task for task in all_tasks if task.id % 2 != 0]

    for task in odd_tasks:
        task.is_finished = True

    Task.objects.bulk_update(odd_tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str):
    final_text = ''

    for char in text:
        new_char = chr(ord(char) - 3)
        final_text += new_char

    Task.objects.filter(title=task_title).update(description=final_text)


# 6

def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
    odd_rooms = [str(room) for room in deluxe_rooms if room.id % 2 == 0]

    return '\n'.join(odd_rooms)


def increase_room_capacity():
    all_rooms = HotelRoom.objects.all().order_by('id')
    previous_capacity = None

    for room in all_rooms:
        if not room.is_reserved:
            continue

        if previous_capacity is None:
            room.capacity += room.id
        else:
            room.capacity += previous_capacity

        previous_capacity = room.capacity

    HotelRoom.objects.bulk_update(all_rooms, ['capacity'])


def reserve_first_room():
    first_room = HotelRoom.objects.first()

    if not first_room.is_reserved:
        first_room.is_reserved = True
        first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()

    if not last_room.is_reserved:
        last_room.delete()


# 7

def update_characters():
    all_characters = Character.objects.all()

    for char in all_characters:
        if char.class_name == 'Mage':
            char.level += 3
            char.intelligence -= 7
        elif char.class_name == 'Warrior':
            char.hit_points /= 2
            char.dexterity += 4
        else:
            char.inventory = 'The inventory is empty'

    fields_to_update = ['level', 'intelligence', 'hit_points', 'dexterity', 'inventory']
    Character.objects.bulk_update(all_characters, fields_to_update)


def fuse_characters(first_character: Character, second_character: Character):
    Character.objects.create(
        name=f'{first_character.name} {second_character.name}',
        class_name='Fusion',
        level=(first_character.level + second_character.level) // 2,
        strength=(first_character.strength + second_character.strength) * 1.2,
        dexterity=(first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence=(first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points=first_character.hit_points + second_character.hit_points,
        inventory='Bow of the Elven Lords, Amulet of Eternal Wisdom' if first_character.class_name in (
        'Mage', 'Scout') else 'Dragon Scale Armor, Excalibur'
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.all().update(dexterity=30)


def grand_intelligence():
    Character.objects.all().update(intelligence=40)


def grand_strength():
    Character.objects.all().update(strength=50)


def delete_characters():
    chars_to_delete = Character.objects.filter(inventory='The inventory is empty')

    chars_to_delete.delete()


# 1

# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))

# 2

# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)

# 3

# print(show_all_locations())
# print(new_capital())
# print(get_capitals())
