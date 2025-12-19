from .TileView import TileView
from game.tile import Tile

class FarmView:
    def __init__(self, parent, rows, cols, start_x, start_y, money, size=30, gap=6):
        self.tiles=[]

        for r in range(rows):
            for c in range(cols):
                x = start_x + c * (size + gap)
                y = start_y + r * (size + gap)
                tile = TileView(parent, x, y, size=size, money=money)
                self.tiles.append(tile)

    def tick(self):
        for tile in self.tiles:
            tile.tick()

    def load_tiles(self, tile_data_list):
        for tile_view, tile_data in zip(self.tiles, tile_data_list):
            tile = Tile.from_dict(tile_data)
            tile_view.set_tile(tile)
