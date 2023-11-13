from .box import Box
from .color import Color
class ColorBox(Box, Color):
    def __init__(self, width, height, color):
        '''
        :param width:
        :param height:
        :param color:
        '''
        super().__init__(width, height)
        Color.__init__(self, color)
    def __str__(self):
        return (f'{super().__str__()}\n'
                f'{Color.__str__(self)}')