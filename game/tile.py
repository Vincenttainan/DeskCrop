from enum import Enum
import time

class TileState(Enum):
    EMPTY = 0
    GROWING = 1
    READY = 2

class Tile:
    def __init__(self, grow_duration=10):
        self.state = TileState.EMPTY
        self.planted_at = None
        self.grow_duration = grow_duration  # 秒

    def plant(self):
        if self.state == TileState.EMPTY:
            self.state = TileState.GROWING
            self.planted_at = time.time()
            print("(game/tile.py)InGameInfo : 種植完成，作物開始生長！")

    def update(self):
        """每次 game loop 呼叫，檢查是否成熟"""
        if self.state == TileState.GROWING:
            if time.time() - self.planted_at >= self.grow_duration:
                self.state = TileState.READY
                print("(game/tile.py)InGameInfo : 作物成熟，可以收成了！")

    def harvest(self):
        if self.state == TileState.READY:
            self.state = TileState.EMPTY
            self.planted_at = None
            print("(game/tile.py)InGameInfo : 收成完成，土地變空！")
            return True  # 可以加錢或其他效果
        return False
    
    def to_dict(self):
        return {
            "state": self.state.name,
            "planted_at": self.planted_at,
            "grow_duration": self.grow_duration
        }
    
    @staticmethod
    def from_dict(data):
        tile = Tile(grow_duration=data["grow_duration"])
        tile.state = TileState[data["state"]]
        tile.planted_at = data["planted_at"]

        tile.update()
        return tile