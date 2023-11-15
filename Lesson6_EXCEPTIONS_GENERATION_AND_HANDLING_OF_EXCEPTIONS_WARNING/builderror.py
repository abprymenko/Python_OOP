class BuildError(Exception):
    def __init__(self, amount:int, limit:int):
        self.Amount:int = amount
        self.Limit:int = limit
    def __str__(self):
        return f'Amount: {self.Amount} is greater than limit: {self.Limit}'