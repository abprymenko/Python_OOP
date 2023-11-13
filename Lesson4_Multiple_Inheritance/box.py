class Box:
    def __init__(self, width:float, height:float):
        self.Width:float = width
        self.Height:float = height
    def __str__(self):
        return (f'Width: {self.Width}\n'
                f'Height: {self.Height}')