gifts = input().split()

index = int
current_gift = ''
gift_to_replace = ''
gift_to_remove = ''

while True:

    current_action = input().split()

    if "Money" in current_action and "No" in current_action:
        break

    if "OutOfStock" in current_action:

        gift_to_remove = current_action[1]

        while gift_to_remove in gifts:
            index = gifts.index(gift_to_remove)
            gifts.pop(index)
            gifts.insert(index, 'None')

    elif "Required" in current_action:

        gift_to_replace = current_action[1]
        index = int(current_action[2])
        if len(gifts) > index >= 0:
            gifts.pop(index)
            gifts.insert(index, gift_to_replace)

    else:

        gifts[-1] = current_action[1]


print(' '.join(str(element) for element in gifts if element != 'None'))