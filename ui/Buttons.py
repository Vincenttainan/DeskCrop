import tkinter as tk

class MacCloseButton:
    # red circle with a X when mouse get close to it
    # ( ) --|mouse close|--> (X) --|mouse leave|--> ( )
    def __init__(
        self,
        parent,
        x=10,
        y=10,
        size=16,
        bg="white",
        command=None
    ):
        self.parent = parent
        self.size = size
        self.command = command or parent.destroy

        self.canvas = tk.Canvas(
            parent,
            width=size,
            height=size,
            highlightthickness=0,
            bg=bg
        )
        self.canvas.place(x=x, y=y)

        self.circle = self.canvas.create_oval(
            0, 0, size, size,
            fill="#ff5f56",
            outline=""
        )

        pad = 4
        self.x1 = self.canvas.create_line(
            pad, pad, size - pad, size - pad,
            fill="black", width=2, state="hidden"
        )
        self.x2 = self.canvas.create_line(
            size - pad, pad, pad, size - pad,
            fill="black", width=2, state="hidden"
        )

        self.canvas.bind("<Enter>", self._on_enter)
        self.canvas.bind("<Leave>", self._on_leave)
        self.canvas.bind("<ButtonPress-1>", self._on_click)

    def _on_enter(self, event):
        self.canvas.focus_set()
        self.canvas.itemconfigure(self.circle, fill="#e0443e")
        self.canvas.itemconfigure(self.x1, state="normal")
        self.canvas.itemconfigure(self.x2, state="normal")

    def _on_leave(self, event):
        self.canvas.itemconfigure(self.circle, fill="#ff5f56")
        self.canvas.itemconfigure(self.x1, state="hidden")
        self.canvas.itemconfigure(self.x2, state="hidden")

    def _on_click(self, event):
        self.command()