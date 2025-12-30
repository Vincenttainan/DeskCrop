from .TileView import TileView
from game import Tile, TileState
from utils.debug import log

class FarmView:
    def __init__(self, parent, rows, cols, start_x, start_y, money, size=30, gap=6):
        self.rows=rows
        self.cols=cols
        self.tiles=[]
        self.unlocked_count=0
        self.money = money

        for r in range(rows):
            for c in range(cols):
                x = start_x + c * (size + gap)
                y = start_y + r * (size + gap)
                tile = TileView(parent,
                                x, y,
                                size=size,
                                money=money,
                                on_unlock_request=self.try_unlock_tile
                                )
                self.tiles.append(tile)

    def try_unlock_tile(self, tile_view):
        if tile_view.tile.state != TileState.LOCKED:
            return

        price = self.get_unlock_price()

        if self.money.spend(price):
            tile_view.tile.unlock()
            self.unlocked_count += 1
            tile_view._update_view()
            log("INFO", "FarmView", f"解鎖土地，花費 {price}")
        else:
            log("WARN", "FarmView", "金錢不足，無法解鎖")


    def get_unlock_price(self):
        return (self.unlocked_count+1)*10

    def unlock(self, r, c):
        if 0 <= r < self.rows and 0 <= c < self.cols:
            idx = r * self.cols + c
            self.tiles[idx].tile.unlock()

    def tick(self):
        for tile in self.tiles:
            tile.tick()

    def load_tiles(self, tile_data_list):
        for tile_view, tile_data in zip(self.tiles, tile_data_list):
            tile = Tile.from_dict(tile_data)
            tile_view.set_tile(tile)
