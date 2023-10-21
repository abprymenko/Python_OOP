from humanrole import HumanRole
from autotype import AutoType
from human import Human
class Auto:
    def __init__(self, model:str, type:AutoType):
        self.Model:str = model
        self.Type:AutoType = type
        self.Passengers:list = list()
        self.Drivers:list = list()
    def AddPassengers(self, human:Human):
        if(human.Role == HumanRole.PASSENGER):
            self.Passengers.append(human)
    def AddDrivers(self, human:Human):
        if(human.Role == HumanRole.DRIVER):
            self.Drivers.append(human)
    def __str__(self):
        drivers:str = ''
        passengers:str = ''
        for driver in self.Drivers:
            drivers+=f'\n{driver.__str__()}'
        for passenger in self.Passengers:
            passengers+=f'\n{passenger.__str__()}'
        return (f'Passengers:\n {passengers}\n'
                f'Drivers:\n {drivers}')