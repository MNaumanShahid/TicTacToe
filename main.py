import random


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

symbol = ["X", "O"]

choice = int(input(f"Choose your symbol out of {symbol}. Enter 1 or 2:"))

player = symbol[choice - 1]
comp = None
for item in symbol:
    if item != player:
        comp = item

# print(player, comp)


def show_board(board_list):
    map = ""
    count = 0
    for e in board_list:
        count += 1
        if count % 3 != 0 and count != 9:
            map += e + " | "
        elif count == 9:
            map += e
        else:
            map += e + "\n---------\n"
    print(map)


moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def make_move():
    player_move = int(input("Enter your move using numer 1-9 sum of row and column: "))
    moves.remove(player_move)
    comp_move = random.choice(moves)
    moves.remove(comp_move)
    return [player_move - 1, comp_move - 1]


def check_win(candidate, board_list):
    winning_pos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for poss in winning_pos:
        check = 0
        for pos in poss:
            if candidate == board_list[pos - 1]:
                check += 1
        if check == 3:
            return True
    return False


def game():
    game_is_on = True
    move = 0
    while game_is_on:
        show_board(board)
        move_list = make_move()
        player_move = move_list[0]
        comp_move = move_list[1]
        board[player_move] = player
        move += 1
        if check_win(player, board):
            show_board(board)
            print("You win.")
            break
        if move == 9:
            show_board(board)
            print("Draw")
            break
        board[comp_move] = comp
        move += 1
        if check_win(comp, board):
            show_board(board)
            print("You lose")
            break


game()