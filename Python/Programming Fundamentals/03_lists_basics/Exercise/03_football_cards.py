a_team = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
b_team = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
a_kicked_players = []
b_kicked_players = []

stopGame = False

cards = input().split(' ')  # adds cards in format "A-1", "A-5"

for element in cards:

    if element[0] == 'A':  # A Team

        if element[2::] not in a_kicked_players:
            a_kicked_players.append(element[2::])
        else:
            continue

    else:  # B Team

        if element[2::] not in b_kicked_players:
            b_kicked_players.append(element[2::])

    if len(a_kicked_players) >= 5 or len(a_kicked_players) >= 5:
        stopGame = True
        break

print(f"Team A - {len(a_team) - len(a_kicked_players)}; Team B - {len(b_team) - len(b_kicked_players)}")

if stopGame:
    print("Game was terminated")
