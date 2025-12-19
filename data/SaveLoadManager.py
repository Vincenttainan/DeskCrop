import json
import os

SAVE_PATH = "data/save.json"

class SaveLoadManager:
    @staticmethod
    def save(money, tiles):
        data = {
            "money": money.amount,
            "tiles": [tile.tile.to_dict() for tile in tiles]
        }

        with open(SAVE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def load():
        if not os.path.exists(SAVE_PATH):
            return None

        with open(SAVE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
