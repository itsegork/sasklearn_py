import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.root = tk.Tk()
        self.root.title("Крестики-нолики")
        self.buttons = []
        
        # СОЗДАНИЕ КНОПОК
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)
        
        self.draw_board()
        self.root.mainloop()

    def draw_board(self):
        for i in range(9):
            self.buttons[i].config(text=self.board[i], state=tk.NORMAL)

    def check_winner(self):
        win_coord = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for line in win_coord:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]]:
                return self.board[line[0]]
        return None

    def player_move(self, index):
        if self.board[index] not in "XO":
            self.board[index] = "X"
            self.buttons[index].config(text="X", state=tk.DISABLED)
            
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Победа", f"{winner} победил!")
                self.reset_board()
            elif all(x in "XO" for x in self.board):
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset_board()
            else:
                self.computer_move()

    def computer_move(self):
        best_score = -float("inf")
        best_move = None
        for i in range(9):
            if self.board[i] not in "XO":
                self.board[i] = "O"
                score = self.minimax(self.board, False)
                self.board[i] = str(i + 1)
                if score > best_score:
                    best_score = score
                    best_move = i

        self.board[best_move] = "O"
        self.buttons[best_move].config(text="O", state=tk.DISABLED)
        
        winner = self.check_winner()
        if winner:
            messagebox.showinfo("Победа", f"{winner} победил!")
            self.reset_board()
        elif all(x in "XO" for x in self.board):
            messagebox.showinfo("Ничья", "Ничья!")
            self.reset_board()

    def minimax(self, board, is_maximizing):
        winner = self.check_winner()
        if winner == "X":
            return -1
        elif winner == "O":
            return 1
        elif all(x in "XO" for x in board):
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for i in range(9):
                if board[i] not in "XO":
                    board[i] = "O"
                    score = self.minimax(board, False)
                    board[i] = str(i + 1)
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] not in "XO":
                    board[i] = "X"
                    score = self.minimax(board, True)
                    board[i] = str(i + 1)
                    best_score = min(score, best_score)
            return best_score

    def reset_board(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.draw_board()

# СОЗДАНИЕ ОБЪЕКТА ИГРЫ
game = TicTacToe()