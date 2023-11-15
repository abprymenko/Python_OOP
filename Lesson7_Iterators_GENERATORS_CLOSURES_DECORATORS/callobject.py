class Helper:
    def __init__(self, work:str):
        self.Work:str = work
    def __call__(self, work:str):
        return f"I will help you with your {self.Work}. Afterwards I will help you with {work}."