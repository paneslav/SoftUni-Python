from collections import deque


def show_board_numeration():
    index = 1
    print(f"This is the numeration of the board:")
    for row in range(board_size):
        print('|', end='')
        for col in range(board_size):
            print(f'  {index}  |' if index < 10 else f'  {index} |', end='')
            index += 1
        print()


def get_players():
    player_one_name = input('Player one name: ')
    player_two_name = input('Player two name: ')
    player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()

    while player_one_symbol not in 'XO':
        player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()

    player_two_symbol = 'X' if player_one_symbol == 'O' else 'O'

    return deque([(player_one_name, player_one_symbol), (player_two_name, player_two_symbol)])


def create_board(board_size):
    board = []

    for row in range(board_size):
        board.append([None] * board_size)

    return board


def assign_board_positions(board):
    positions = {}
    start = 1
    for row in range(len(board[0])):
        for col in range(len(board[0])):
            positions[start] = (row, col)
            start += 1

    return positions


def print_board(board):
    for row in range(len(board[0])):
        print('|', end='')
        for col in range(len(board[0])):
            print(f'  {board[row][col]}  |' if board[row][col] is not None else f"  {' '}  |", end='')
        print()


def draw_check(board):
    for row in board:
        if None in row:
            return False

    return True


def win_check(board, symbol, row, col):
    def check_horizontal():
        for item in board[row]:
            if item != symbol:
                return False

        return True

    def check_vertical():
        for r in range(len(board)):
            if board[r][col] != symbol:
                return False

        return True

    def check_main_diagonal():
        for i in range(len(board)):
            if board[i][i] != symbol:
                return False

        return True

    def check_secondary_diagonal():
        for i in range(len(board)):
            if board[i][-1 - i] != symbol:
                return False

        return True

    return check_horizontal() or check_vertical() or check_main_diagonal() or check_secondary_diagonal()


def play(board, players_info, positions):
    print(f"{players_info[0][0]} starts first!")

    while True:
        players_name = players_info[0][0]
        players_symbol = players_info[0][1]

        try:
            players_choice = int(input(f'{players_name} choose a free position [1-{board_size * board_size}]: '))
        except (KeyError, ValueError):
            print(f"The position you chose is invalid")
            continue

        row, col = positions[players_choice]

        if board[row][col] is not None:
            print(f"The position you chose has been already taken, please select another!")
            continue

        board[row][col] = players_symbol

        if win_check(board, players_symbol, row, col):
            print(f"{players_name} won!")
            break

        if draw_check(board):
            print(f"Draw!")
            break

        print_board(board)

        players_info[0], players_info[1] = players_info[1], players_info[0]


board_size = 3
board = create_board(board_size)
board_positions = assign_board_positions(board)

players_info = get_players()
show_board_numeration()
play(board, players_info, board_positions)
