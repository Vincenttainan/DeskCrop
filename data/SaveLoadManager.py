import json
import os
from utils.debug import log

SAVE_PATH = "data/save.json"

class SaveLoadManager:
    @staticmethod
    def save(money, FarmView, tiles):
        log("INFO", "data/SaveLoadManager.py", "開始存檔")
        data = {
            "money": money.amount,
            "unlocked_count": FarmView.unlocked_count,
            "tiles": [tile.tile.to_dict() for tile in tiles]
        }

        with open(SAVE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        log("INFO", "data/SaveLoadManager.py", "存檔完成")

    @staticmethod
    def load():
        log("INFO", "data/SaveLoadManager.py", "開始讀檔")
        if not os.path.exists(SAVE_PATH):
            log("INFO", "data/SaveLoadManager.py", "沒有檔案")
            return None

        with open(SAVE_PATH, "r", encoding="utf-8") as f:
            log("INFO", "data/SaveLoadManager.py", "讀檔完成")
            return json.load(f)
