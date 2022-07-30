def is_winning(ticket):

    if len(ticket) != 20:
        return 'invalid ticket'

    left_side = ticket[:10]
    right_side = ticket[10:]

    for symbol in winning_symbols:
        if symbol in ticket:
            for repetitions in range(10,5, -1):
                if symbol * repetitions in left_side and symbol * repetitions in right_side:
                    if repetitions == 10:
                        return f'ticket "{ticket}" - {repetitions}{symbol} Jackpot!'
                    return f'ticket "{ticket}" - {repetitions}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets_list = [ticket.strip() for ticket in input().split(', ')]

winning_symbols = ['@', '#', '$', '^']

for ticket in tickets_list:
    print(is_winning(ticket))
