from tkinter import *
import random

board = {}


def update_board(clear=False):
    for row in range(3):
        for col in range(3):
            if clear: board[(row, col)]["value"] = ""
            board[(row, col)]["button"]["text"] = board[(row, col)]["value"]


def enable_board(state):
    for row in range(3):
        for col in range(3):
            board[(row, col)]["button"]["state"] = "normal" if state else "disabled"


def new_game():
    update_board(clear=True)
    enable_board(True)
    status_text["text"] = "Ваш ход"


def make_move(row, col, who):
    board[(row, col)]["value"] = who
    update_board()
    if win_check(who):
        status_text["text"] = f"Вы {'выиграли' if who == 'X' else 'проиграли'} !"
        enable_board(False)
        return True
    if all(board[(row, col)]["value"] for row in range(3) for col in range(3)):
        status_text["text"] = "Ничья!"
        enable_board(False)
        return True
    return False


def ai_move():
    positions = [(row, col) for row in range(3) for col in range(3) if not board[(row, col)]["value"]]
    for pos in positions:
        for who in "XO":
            board[pos]["value"] = who
            win = win_check(who)
            board[pos]["value"] = ""
            if win:
                return pos

    return random.choice(positions)


def win_check(who):
    win = all(board[(i, i)]["value"] == who for i in range(3))
    win |= all(board[(i, 2 - i)]["value"] == who for i in range(3))
    for i in range(3):
        win |= all(board[(i, col)]["value"] == who for col in range(3))
        win |= all(board[(row, i)]["value"] == who for row in range(3))
    return win


def game(row, col):
    if board[(row, col)]["value"]:  # already occupied
        return
    if make_move(row, col, "X"):
        return

    make_move(*ai_move(), "O")


def resize_board(event):
    main_screen["width"] = main_screen.winfo_height()


root = Tk()
root.title("Крестики-нолики")
root.config(bg='black')

heading_frame = Frame(root, bg='black', highlightthickness=3, highlightbackground='silver', height=100)
heading_frame.pack(fill=X)
status_text = Label(heading_frame, text="Ваш ход", bg='black', fg='white', font='Baskerville 16')
status_text.pack(anchor="center")

bottom_frame = Frame(root, bg='black')
bottom_frame.pack(fill=X, side=BOTTOM)
Button(bottom_frame, text='Новая игра', bg='green', fg='black', command=new_game, font='Elephant 12').pack(side=LEFT)
Button(bottom_frame, text='Выйти', bg='red', fg='black', command=root.destroy, font='Elephant 12').pack(side=RIGHT)

main_screen = Frame(root, bg='black', width=420, height=420)
main_screen.pack(side=RIGHT, fill=Y)
main_screen.columnconfigure(tuple(range(3)), minsize=140, weight=1, uniform="board")
main_screen.rowconfigure(tuple(range(3)), minsize=140, weight=1, uniform="board")
main_screen.bind("<Configure>", resize_board)
main_screen.grid_propagate(False)

for row in range(3):
    for col in range(3):
        board[(row, col)] = {"value": "", "button": Button(main_screen, border=0, font='CASTELLAR 48 bold',
                                                           command=lambda r=row, c=col: game(r, c))}
        board[(row, col)]["button"].grid(row=row, column=col, sticky="news", padx=5, pady=5)

root.mainloop()
