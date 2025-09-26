import tkinter as tk
from tkinter import messagebox
import random

root=tk.Tk()
root.title("Крестики-нолики")
root.iconbitmap("icon1.ico")

current_player="X"
buttons=[]

def check_winner(player):
    winning_combinations = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in winning_combinations:
        a,b,c=combo
        if buttons[a]["text"]==buttons[b]["text"]==buttons[c]["text"]==player:
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")
            return True
    return False


def check_win_temp(board, player):
    winning_combinations = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in winning_combinations:
        a,b,c=combo
        if board[a]==board[b]==board[c]==player:
            return True
    return False


def on_click(index):
    global current_player
    if buttons[index]["text"]=="" and current_player=="X":
        buttons[index]["text"]="X"

        if check_winner("X"):
            messagebox.showinfo("Победа","X победил!")
            return

        if all(button["text"]!="" for button in buttons):
            messagebox.showinfo("Ничья","Game Over. Ничья")
            return
        current_player="O"
        root.after(500,computer_turn)

def computer_turn():
    global current_player

    board=[button["text"] for button in buttons]
    empty_cells=[i for i in range(9) if board[i]==""]

    if not empty_cells:
        return

    for i in empty_cells:
        temp_board=board.copy()
        temp_board[i]="O"
        if check_win_temp(temp_board, "O"):
            buttons[i]["text"]="O"
            break
    else:
        for i in empty_cells:
            temp_board=board.copy()
            temp_board[i]="X"
            if check_win_temp(temp_board, "X"):
                buttons[i]["text"]="O"
                break
        else:
            if board[4]=="":  # Центр
                buttons[4]["text"]="O"
            else:
                corners=[0,2,6,8]
                empty_corners=[c for c in corners if board[c]==""]
                if empty_corners:
                    buttons[random.choice(empty_corners)]["text"]="O"
                else:
                    buttons[random.choice(empty_cells)]["text"]="O"

    if check_winner("O"):  # Передаем "O" как параметр
        messagebox.showinfo("Победа","O победил!")
        return

    if all(button["text"]!= "" for button in buttons):
        messagebox.showinfo("Ничья","Game Over. Ничья")
        return

    current_player="X"


def reset_game():
    global current_player
    current_player="X"
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
for i in range(9):
    button=tk.Button(
        root,
        text="",
        font=("Arial", 30),
        width=5,
        height=2,
        command=lambda idx=i: on_click(idx)
    )
    button.grid(row=i //3, column=i % 3)
    buttons.append(button)

reset_button = tk.Button(root, text="Новая игра", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

root.mainloop()