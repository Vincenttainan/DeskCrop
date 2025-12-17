import tkinter as tk
from game.tile import Tile, TileState

class TileView:
    def __init__(self, parent, x, y, size=30):
        self.parent = parent
        self.size = size
        self.tile = Tile(grow_duration=5)  # 測試用短時間
        self.canvas = tk.Canvas(parent, width=size, height=size, bg="saddle brown")
        self.canvas.place(x=x, y=y)

        self.canvas.bind("<Enter>", self._on_enter)
        self._update_view()

    '''def on_click(self, event):
        if self.tile.state == TileState.EMPTY:
            self.tile.plant()
        elif self.tile.state == TileState.READY:
            self.tile.harvest()
        self._update_view()'''

    def _on_enter(self, event):
        if self.tile.state == TileState.EMPTY:
            self.tile.plant()
        elif self.tile.state == TileState.READY:
            self.tile.harvest()
        self._update_view()

    def _update_view(self):
        """根據 tile 狀態改變顏色"""
        if self.tile.state == TileState.EMPTY:
            self.canvas.config(bg="saddle brown")
        elif self.tile.state == TileState.GROWING:
            self.canvas.config(bg="green")
        elif self.tile.state == TileState.READY:
            self.canvas.config(bg="yellow")

    def tick(self):
        """每個 interval 呼叫一次，更新成長狀態"""
        self.tile.update()
        self._update_view()
