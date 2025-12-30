import tkinter as tk
from game import Tile, TileState
from utils.debug import log

class TileView:
    def __init__(self, parent, x, y, money, size=30, on_unlock_request=None):
        #log("INFO", "ui/TileView.py", "畫布初始化")
        self.parent = parent
        self.size = size
        self.tile = Tile(grow_duration=5)  # 測試用短時間
        self.canvas = tk.Canvas(parent, width=size, height=size, bg="saddle brown")
        self.canvas.place(x=x, y=y)
        self.money=money
        self.on_unlock_request=on_unlock_request

        self.canvas.bind("<Enter>", self._on_enter)
        self.canvas.bind("<ButtonPress-1>", self._on_click)
        self._update_view()

    def _on_click(self, event):
        if self.tile.state == TileState.LOCKED:
            log("INFO", "ui/TileView.py", "畫布被點擊了")
            self.on_unlock_request(self)
        else:
            return

    def _on_enter(self, event):
        self.canvas.focus_set()
        if self.tile.state == TileState.LOCKED:
            return
        log("INFO", "ui/TileView.py", "畫布被入了")
        if self.tile.state == TileState.EMPTY:
            self.tile.plant()
        elif self.tile.state == TileState.READY:
            self.tile.harvest()
            self.money.add(1)
        self._update_view()

    def _update_view(self):
        if self.tile.state == TileState.LOCKED:
            self.canvas.config(bg="black")
        elif self.tile.state == TileState.EMPTY:
            self.canvas.config(bg="saddle brown")
        elif self.tile.state == TileState.GROWING:
            self.canvas.config(bg="green")
        elif self.tile.state == TileState.READY:
            self.canvas.config(bg="yellow")

    def tick(self):
        """每個 interval 呼叫一次，更新成長狀態"""
        self.tile.update()
        self._update_view()

    def set_tile(self, tile):
        self.tile = tile
        self._update_view()

