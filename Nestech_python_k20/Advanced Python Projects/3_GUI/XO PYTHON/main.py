import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.current_player = "X"

        self.cells = []
        for row in range(3):
            cell_row = []
            for col in range(3):
                cell = tk.Button(self.window, text="", font=("Helvetica", 50), width=3, height=1,
                                 command=lambda row=row, col=col: self.play(row, col))
                cell.grid(row=row, column=col)
                cell_row.append(cell)
            self.cells.append(cell_row)

    def play(self, row, col):
        if self.cells[row][col]["text"] == "":
            self.cells[row][col]["text"] = self.current_player

        if self.check_win(row, col):
            self.game_over(self.current_player)
        elif self.check_draw():
            self.game_over("Draw")
        else:
            self.switch_player()


    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self, row, col):
        return (self.cells[row][0]["text"] == self.cells[row][1]["text"] == self.cells[row][2]["text"] == self.current_player or
            self.cells[0][col]["text"] == self.cells[1][col]["text"] == self.cells[2][col]["text"] == self.current_player or
            self.cells[0][0]["text"] == self.cells[1][1]["text"] == self.cells[2][2]["text"] == self.current_player or
            self.cells[0][2]["text"] == self.cells[1][1]["text"] == self.cells[2][0]["text"] == self.current_player)


    def check_draw(self):
        for row in self.cells:
            for cell in row:
                if cell["text"] == "":
                    return False
        return True

    def game_over(self, winner=None):
        for row in self.cells:
            for cell in row:
                cell.config(state="disabled")

        if winner:
            tk.messagebox.showinfo("Game Over", f"{winner} wins!")
        else:
            tk.messagebox.showinfo("Game Over", "It's a draw!")

        self.window.quit()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
