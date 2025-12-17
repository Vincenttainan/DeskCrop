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

# 放置 3 x 2 塊土地
tiles = []
rows = 3
cols = 2
size = 30
gap = 6
start_x = 50
start_y = 50
for row in range(rows):
    for col in range(cols):
        x = start_x + row * ( size + gap )
        y = start_y + col * ( size + gap )
        tile = TileView(parent=root, x=x, y=y, size=size)
        tiles.append(tile)

# 每 500ms 更新一次
def game_loop():
    for tile in tiles:
        tile.tick()
    root.after(500, game_loop)

game_loop()
root.mainloop()
