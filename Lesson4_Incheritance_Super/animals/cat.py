from animal import Animal

class Cat(Animal):
    def __init__(self, age:float, nick:str, breed:str, sound:str):
        super().__init__(age, nick, breed, sound)
    '''
    def __str__(self):
        return (f'Length - {self.length}\n'
                f'Color - {super()._color}\n'
                f'Eyes color - {super().__eyescolor}')
    '''
    '''
        def Speak(self):
            return self.Sound
    '''