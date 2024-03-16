from .box import Box
from .color import Color
class ColorBox(Box, Color):
    def __init__(self, width: float, height: float, colorStr: str, colorAnsi: str):
        '''
        :param width:
        :param height:
        :param colorStr:
        '''
        super().__init__(width, height)
        Color.__init__(self, colorStr, colorAnsi)
    def __str__(self):
        return (f'{super().__str__()}\n'
                f'{Color.__str__(self)}')