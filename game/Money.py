class Money:
    def __init__(self, initial=0):
        self.amount = initial

    def add(self, value: int):
        self.amount += value

    def spend(self, value: int) -> bool:
        if self.amount >= value:
            self.amount -= value
            return True
        return False
