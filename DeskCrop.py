import tkinter as tk
from game import Money
from ui import *
from data.SaveLoadManager import SaveLoadManager

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

money = Money()
save_data = SaveLoadManager.load()

farm = FarmView(
    parent=root,
    rows=5,
    cols=5,
    start_x=50,
    start_y=20,
    size=20,
    gap=6,
    money=money
)

if save_data:
    money.set(save_data["money"])
    farm.load_tiles(save_data["tiles"])
    farm.unlock_count=save_data["unlocked_count"]
else:
    money.set(0)
    farm.unlock(0,0)
    farm.unlock(0,1)
    farm.unlock(0,2)

# init money
Money_View = MoneyView(parent=root, money=money)

# 放按鈕
def save_and_exit():
    save_game()
    root.destroy()

MacCloseButton(parent=root, x=10, y=10, command=save_and_exit)

# 每 0.1sec 更新一次
def game_loop():
    farm.tick()
    Money_View.update()
    root.after(100, game_loop)

def save_game():
    SaveLoadManager.save(money, farm, farm.tiles)

game_loop()
root.mainloop()
