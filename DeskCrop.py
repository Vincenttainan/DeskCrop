import tkinter as tk
from ui import MacCloseButton
from ui import TileView

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = screen_width
window_height = 150
x = (screen_width - window_width) // 2
y = (screen_height - window_height) - 30
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.update_idletasks()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.title("DeskCrop")

# 放按鈕
MacCloseButton(parent=root, x=10, y=10, command=root.destroy)

# 放第一塊土地
tile = TileView(parent=root, x=100, y=50)

# 每 500ms 更新一次
def game_loop():
    tile.tick()
    root.after(500, game_loop)

game_loop()
root.mainloop()
