from os import linesep


def add_songs(*args):
    song_collection = {}
    result = ''
    for item in args:
        song_name = item[0]
        song_lyrics_list = item[-1]

        if song_name in song_collection:
            [song_collection[song_name].append(x) for x in song_lyrics_list]
            continue

        song_collection[song_name] = song_lyrics_list

    for song, lyrics in song_collection.items():
        result += f'- {song}{linesep}'
        if lyrics:
            result += '\n'.join(lyrics) + linesep

    return result


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))

# print(add_songs(
#     ("Beat It", []),
#     ("Beat It",
#      ["Just beat it (beat it), beat it (beat it)",
#       "No one wants to be defeated"]),
#     ("Beat It", []),
#     ("Beat It",
#      ["Showin' how funky and strong is your fight",
#       "It doesn't matter who's wrong or right"]),
# ))

# print(add_songs(
#     ("Love of my life",
#      ["Love of my life, you've hurt me",
#       "You've broken my heart, and now you leave me",
#       "Love of my life, can't you see?",
#       "Bring it back, bring it back"]),
#     ("Beat It", []),
#     ("Love of my life",
#      ["Don't take it away from me",
#       "Because you don't know",
#       "What it means to me"]),
#     ("Dream On",
#      ["Every time that I look in the mirror"]),
# ))
