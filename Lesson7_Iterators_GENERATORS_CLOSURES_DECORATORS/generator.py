class Generator:
    def __init__(self, students:list()):
        self.Students:list() = students
    def GetStyudents(self):
        for i in self.Students:
            yield i
