class Counter:
    def __init__(self, i:int, maxNumber:int):
        self.I:int = i
        self.MaxNumber:int = maxNumber
    def __str__(self):
        return f'Call __str__(self) = {self.I}'
    def __iter__(self):
        self.I = 0
        return  self
    def __next__(self):
        self.I += 1
        if(self.I > self.MaxNumber):
            raise StopIteration
        return self