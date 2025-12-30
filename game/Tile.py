from utils.debug import log
from enum import Enum
import time

class TileState(Enum):
    LOCKED = -1
    EMPTY = 0
    GROWING = 1
    READY = 2

class Tile:
    def __init__(self, grow_duration=10):
        self.state = TileState.LOCKED
        self.planted_at = None
        self.grow_duration = grow_duration  # 秒
        #log("INFO", "data/Tile.py", "初始化一塊地")

    def unlock(self):
        if self.state == TileState.LOCKED:
            self.state = TileState.EMPTY
            log("INFO", "data/Tile.py", "解鎖一塊土地")

    def plant(self):
        if self.state == TileState.EMPTY:
            self.state = TileState.GROWING
            self.planted_at = time.time()
            log("INFO", "data/Tile.py", "種植完成")

    def update(self):
        if self.state == TileState.GROWING:
            if time.time() - self.planted_at >= self.grow_duration:
                self.state = TileState.READY
                log("INFO", "data/Tile.py", "作物成熟")

    def harvest(self):
        if self.state == TileState.READY:
            self.state = TileState.EMPTY
            self.planted_at = None
            log("INFO", "data/Tile.py", "收成完成")
            return True  # 可以加錢或其他效果
        return False
    
    def to_dict(self):
        #log("INFO", "data/Tile.py", "回傳轉字典資訊")
        return {
            "state": self.state.name,
            "planted_at": self.planted_at,
            "grow_duration": self.grow_duration
        }
    
    @staticmethod
    def from_dict(data):
        #log("INFO", "data/Tile.py", "讀取字典資訊")
        tile = Tile(grow_duration=data["grow_duration"])
        tile.state = TileState[data["state"]]
        tile.planted_at = data["planted_at"]

        tile.update()
        return tile