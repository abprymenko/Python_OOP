class Counter:
    def __init__(self, min:int, max:int):
        self.Min:int = min
        self.Max:int = max
    def __iter__(self):
        return  self
    def __next__(self):
        self.Min += 1
        if(self.Min > self.Max):
            raise StopIteration
        return self.Min