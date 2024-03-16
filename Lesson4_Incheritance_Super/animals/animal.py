class Animal:
    length:float = 25.7
    _color:str = "brown"
    __eyescolor:str = "blue"
    def __init__(self, age:float, nick:str, breed:str, sound:str):
        self.Age:float = age
        self.Nick:str = nick
        self.Breed:str = breed
        self.Sound:str = sound
    def __str__(self):
        return (f'Nick - {self.Nick}\n'
                f'Age - {self.Age}\n'
                f'Breed - {self.Breed}')
    def Speak(self):
        #pass
        return self.Sound