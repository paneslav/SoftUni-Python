deck_of_cards = input().split(' ')
loop_count = int(input())

shuffled_list = []
start = [deck_of_cards[0]]
end = [deck_of_cards[-1]]

first_half = deck_of_cards[1:(len(deck_of_cards)//2)]
second_half = deck_of_cards[(len(deck_of_cards)//2):-1]

for i in range(loop_count):

    while len(first_half) != 0 and len(second_half) != 0:
        shuffled_list.append(second_half.pop(0))
        shuffled_list.append(first_half.pop(0))

    first_half = shuffled_list[:(len(shuffled_list) // 2)]
    second_half = shuffled_list[(len(shuffled_list) // 2):]

    shuffled_list = []

shuffled_list = start + first_half + second_half + end

print(shuffled_list)