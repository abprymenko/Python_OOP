class Color:
    def __init__(self, colorStr: str, colorAnsi: str):
        self.ColorStr: str = colorStr
        self.ColorAnsi: str = colorAnsi

    def __str__(self):
        return f'Color: {self.ColorStr}'
