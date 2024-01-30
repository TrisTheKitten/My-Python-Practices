import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

        self.player_turn_label = tk.Label(self.window, text=f"Player {self.current_player}'s turn", font=('Arial', 12))
        self.player_turn_label.grid(row=3, columnspan=3)

        self.buttons = [tk.Button(self.window, text=' ', command=lambda i=i: self.make_move(i), font=('Arial', 24), width=5, height=2) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.buttons[position]['text'] = self.current_player
            if self.check_win(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.quit()
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "The game is a draw!")
                self.window.quit()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.player_turn_label['text'] = f"Player {self.current_player}'s turn"
        else:
            messagebox.showinfo("Invalid Move", "This spot is already taken!")

    def check_win(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        return any(self.board[i] == self.board[j] == self.board[k] == player for i, j, k in win_conditions)

if __name__ == "__main__":
    game = TicTacToe()
    game.window.mainloop()
