import tkinter as tk
import random

root = tk.Tk()
root.title("AI vs You - Tic Tac Toe")
root.geometry("360x520")
root.configure(bg="#6F7F85")

board = [""] * 9
buttons = []

title = tk.Label(root,
                 text="AI vs You",
                 font=("Arial",18,"bold"),
                 bg="#f5f5f5")
title.pack(pady=5)

turn_label = tk.Label(root,
                      text="Your turn – choose a box",
                      font=("Arial",12),
                      bg="#f5f5f5")
turn_label.pack()

frame = tk.Frame(root)
frame.pack(pady=10)


wins = [(0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)]

def check_winner(player):
    for a,b,c in wins:
        if board[a]==board[b]==board[c]==player:
            return True
    return False

def draw():
    return "" not in board

def restart_game():
    for i in range(9):
        board[i] = ""
        buttons[i]["text"] = ""
    turn_label.config(text="Your turn – choose a box")


def show_result(message):

    popup = tk.Toplevel(root)
    popup.title("Game Result")
    popup.geometry("260x150")
    popup.configure(bg="lightgray")   

    label = tk.Label(popup,
                     text=message,
                     font=("Arial",14,"bold"),
                     bg="lightgray")  
    label.pack(pady=25)

    def close_and_reset():
        popup.destroy()
        restart_game()

    ok_btn = tk.Button(popup,
                       text="OK",
                       width=10,
                       bg="white")   
    ok_btn.config(command=close_and_reset)
    ok_btn.pack()


def ai_move():

    turn_label.config(text="AI thinking...")

   
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            if check_winner("O"):
                buttons[i]["text"] = "O"
                show_result(" AI won!")
                return
            board[i] = ""

    
    for i in range(9):
        if board[i] == "":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                buttons[i]["text"] = "O"
                return
            board[i] = ""

    
    empty = [i for i in range(9) if board[i] == ""]
    if empty:
        move = random.choice(empty)
        board[move] = "O"
        buttons[move]["text"] = "O"

    if check_winner("O"):
        show_result(" AI won!")

    elif draw():
        show_result(" It's a Draw!")

    else:
        turn_label.config(text="Your turn – choose a box")


def click(i):

    if board[i] == "":
        board[i] = "X"
        buttons[i]["text"] = "X"

        if check_winner("X"):
            show_result("Congrats! You won!")

        elif draw():
            show_result(" It's a Draw!")

        else:
            root.after(500, ai_move)


for i in range(9):

    btn = tk.Button(frame,
                    text="",
                    font=("Arial",24,"bold"),
                    width=4,
                    height=2,
                    bg="white",
                    command=lambda i=i: click(i))

    btn.grid(row=i//3, column=i%3, padx=5, pady=5)

    buttons.append(btn)

control_frame = tk.Frame(root, bg="#f5f5f5")
control_frame.pack(pady=10)


clear_btn = tk.Button(control_frame,
                      text="Clear",
                      font=("Arial",11),
                      width=11,
                      command=restart_game)
clear_btn.grid(row=0, column=1, padx=10)

quit_btn = tk.Button(control_frame,
                     text="Quit",
                     font=("Arial",11),
                     width=10,
                     command=root.destroy)
quit_btn.grid(row=0, column=2, padx=10)

root.mainloop()