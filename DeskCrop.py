import tkinter as tk
import ui

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = screen_width
window_height = 150
x = (screen_width - window_width) // 2
y = (screen_height - window_height) - 30

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.title("DeskCrop")
root.update_idletasks()
root.overrideredirect(True)
root.attributes("-topmost", True)

ui.MacCloseButton(
    parent=root,
    x=10,
    y=10,
    command=root.destroy
)

root.mainloop()