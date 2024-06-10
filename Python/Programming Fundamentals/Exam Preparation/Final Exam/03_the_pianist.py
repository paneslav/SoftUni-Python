def fill_collection(music_collection, music_piece, composer, key):
    music_collection[music_piece] = {'composer': composer, 'key': key}


def add_to_collection(music_collection, music_piece, composer, key):
    if music_piece in music_collection:
        print(f"{music_piece} is already in the collection!")
    else:
        music_collection[music_piece] = {'composer': composer, 'key': key}
        print(f"{music_piece} by {composer} in {key} added to the collection!")


def remove_from_collection(music_collection, music_piece):
    if music_piece in music_collection:
        print(f"Successfully removed {music_piece}!")
        del music_collection[music_piece]
    else:
        print(f"Invalid operation! {music_piece} does not exist in the collection.")


def change_key(music_collection, new_key, music_piece):
    if music_piece in music_collection:
        music_collection[music_piece]['key'] = new_key
        print(f"Changed the key of {music_piece} to {new_key}!")
    else:
        print(f"Invalid operation! {music_piece} does not exist in the collection.")


number_of_pieces = int(input())

music_collection = {}

for i in range(number_of_pieces):
    command = input().split('|')

    music_piece = command[0]
    composer = command[1]
    key = command[-1]

    fill_collection(music_collection, music_piece, composer, key)

while True:
    command = input().split('|')
    if command[0] == 'Stop':
        break

    operation = command[0]
    music_piece = command[1]

    if operation == 'Add':
        composer = command[2]
        key = command[-1]

        add_to_collection(music_collection, music_piece, composer, key)

    elif operation == 'Remove':
        remove_from_collection(music_collection, music_piece)

    elif operation == 'ChangeKey':
        new_key = command[2]
        change_key(music_collection, new_key, music_piece)


for piece, composer in music_collection.items():
    print(f"{piece} -> Composer: {music_collection[piece]['composer']}, Key: {music_collection[piece]['key']}")