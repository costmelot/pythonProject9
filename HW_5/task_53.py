# Создайте программу для игры в ""Крестики-нолики"".

import random
import time


def print_board(board):
    print("\n    1   2   3 \n")
    print("1   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("   ---+---+---")
    print("2   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("   ---+---+---")
    print("3   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "\n")


def check_row(board, row):
    return (board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != " ")


def check_column(board, col):
    return (board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != " ")


def check_diagonals(board):
    return (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ") or \
           (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != " ")


def check_winner(board):
    for i in range(3):
        if check_row(board, i):
            return True
        if check_column(board, i):
            return True
    if check_diagonals(board):
        return True
    return False


def is_board_full(board):
    for item in board:
        if " " in item:
            return False
    return True


def play(board):
    while True:
        row = input("Введите номер строки: ")
        while not row.isdigit() or int(row) < 1 or int(row) > 3:
            row = input("Введите номер строки от 1 до 3: ")
        row = int(row)
        col = input("Введите номер столбца: ")
        while not col.isdigit() or int(col) < 1 or int(col) > 3:
            col = input("Введите номер столбца от 1 до 3: ")
        col = int(col)
        if board[row - 1][col - 1] != " ":
            print("Выберите пустую ячейку!")
        else:
            return (row - 1, col - 1)


def play_random(board):
    possible_moves = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == " ":
                possible_moves.append((row, col))

    return possible_moves[random.randrange(len(possible_moves))]


def main():
    random.seed(time.time())
    print("\n== Крестики-нолики ==")
    # Создаем поле для игры
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    # Cоздаем 2 игроков
    players = ["X", "O"]
    # Игрок Х ходит первым
    turn = 0
    while not is_board_full(board):
        print_board(board)
        if turn == 0:
            print("Ваш ход!")
            row, col = play(board)
            board[row][col] = players[turn]

        else:
            # Играет компьютер
            print("Компьютер делает ход!")
            row, col = play_random(board)
            board[row][col] = players[turn]
        # Провереям выиграли кто-то из игроков
        if check_winner(board):
            print_board(board)
            print("Вы выиграли!" if turn == 0 else "Вы проиграли!")
            break

        # Выбираем другого игрока
        turn = 1 - turn

    else:
        print_board(board)
        print("Ничья!")


main()
