import random

ai_random = random.randint(1000, 4000)

ai_list = [i for i in str(ai_random)]

players_guess = []
bulls_counter = 0
cows_counter = 0

while True:

    user_input = input("Please place your guess: ")

    if user_input == str(ai_random):
        print(f"You win! The number was: {ai_random}")
        break

    players_guess += [index for index in user_input]

    for y in range(len(ai_list)):  # 2446 - 2236 2 bika 1 krava -
        if players_guess[y] == ai_list[y]:
            bulls_counter += 1
        elif players_guess[y] in ai_list:
            if players_guess.count(f"{players_guess[y]}") >= 2:
                continue
            cows_counter += 1

    print(f"{bulls_counter} бика и {cows_counter} крави.")
    players_guess = []
    bikove_counter = 0
    kravi_counter = 0