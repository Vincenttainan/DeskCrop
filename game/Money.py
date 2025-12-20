from utils.debug import log

class Money:
    def __init__(self, initial=0):
        self.amount = initial
        log("INFO", "data/Money.py", "初始化錢")

    def add(self, value: int):
        self.amount += value
        log("INFO", "data/Money.py", f"錢 + {value}")
    
    def set(self, value: int):
        self.amount = value
        log("INFO", "data/Money.py", f"設定錢 = {value}")

    def spend(self, value: int) -> bool:
        if self.amount >= value:
            self.amount -= value
            log("INFO", "data/Money.py", f"花錢 {value} 元成功，剩下 {self.amount}")
            return True
        log("INFO", "data/Money.py", f"花錢 {value} 元失敗，原本 {self.amount}")
        return False
