import tkinter as tk

class MoneyView:
    def __init__(self, parent, money, x=10, y=50):
        self.money = money
        self.label = tk.Label(
            parent,
            text=f"$ {self.money.amount}",
            font=("Helvetica", 14),
            fg="gold"
        )
        self.label.place(x=x, y=y)

    def update(self):
        self.label.config(text=f"$ {self.money.amount}")
