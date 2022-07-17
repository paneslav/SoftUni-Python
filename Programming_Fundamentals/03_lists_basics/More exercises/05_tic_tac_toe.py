first_line = input().split()
second_line = input().split()
third_line = input().split()

player_one_winCondition = False
player_two_winCondition = False

#  column check
if first_line[0] == second_line[0] and first_line[0] == third_line[0]:

    if first_line[0] == "1":
        player_one_winCondition = True
    elif first_line[0] == "2":
        player_two_winCondition = True
elif first_line[1] == second_line[1] and first_line[1] == third_line[1]:

    if first_line[0] == "1":
        player_one_winCondition = True
    elif first_line[0] == "2":
        player_two_winCondition = True
elif first_line[2] == second_line[2] and first_line[2] == third_line[2]:

    if first_line[0] == "1":
        player_one_winCondition = True
    elif first_line[0] == "2":
        player_two_winCondition = True

#  row check
if first_line.count("1") == 3 or second_line.count("1") == 3 or third_line.count("1") == 3:
    player_one_winCondition = True
elif first_line.count("2") == 3 or second_line.count("2") == 3 or third_line.count("2") == 3:
    player_two_winCondition = True

#  diagonal check
if first_line[0] == second_line[1] and first_line[0] == third_line[2]:

    if first_line[0] == "1":
        player_one_winCondition = True
    elif first_line[0] == "2":
        player_two_winCondition = True
elif first_line[-1] == second_line[1] and first_line[-1] == third_line[0]:

    if first_line[-1] == "1":
        player_one_winCondition = True
    elif first_line[-1] == "2":
        player_two_winCondition = True

#  print result
if player_one_winCondition:
    print("First player won")
elif player_two_winCondition:
    print("Second player won")
else:
    print("Draw!")