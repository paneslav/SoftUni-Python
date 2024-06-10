favourite_genres = [item.strip() for item in input().split(' | ')]

while True:
    command = input().split()
    if command[0] == 'Stop!':
        break

    action = command[0]

    if action == 'Join':
        genre = command[-1]
        if genre not in favourite_genres:
            favourite_genres.append(genre)

    elif action == 'Drop':
        genre = command[-1]
        if genre in favourite_genres:
            favourite_genres.remove(genre)

    elif action == 'Replace':
        old_genre = command[1]
        new_genre = command[-1]
        if old_genre in favourite_genres and new_genre not in favourite_genres:
            old_index = favourite_genres.index(old_genre)
            favourite_genres.pop(old_index)
            favourite_genres.insert(old_index, new_genre)
    elif action == 'Prefer':
        first_index = int(command[1])
        second_index = int(command[-1])

        if first_index < len(favourite_genres) and second_index < len(favourite_genres):
            favourite_genres[first_index], favourite_genres[second_index] = favourite_genres[second_index], favourite_genres[first_index]

print(' '.join(favourite_genres))