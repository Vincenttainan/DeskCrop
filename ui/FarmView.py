from .TileView import TileView

class FarmView:
    def __init__(self, parent, rows, cols, start_x, start_y, size=30, gap=6):
        self.tiles = []

        for r in range(rows):
            for c in range(cols):
                x = start_x + c * (size + gap)
                y = start_y + r * (size + gap)
                tile = TileView(parent, x, y, size=size)
                self.tiles.append(tile)

    def tick(self):
        for tile in self.tiles:
            tile.tick()
