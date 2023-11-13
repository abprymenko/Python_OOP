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
        drivers = '\n'.join(driver.__str__() for driver in self.Drivers)
        passengers = '\n'.join(passenger.__str__() for passenger in self.Passengers)
        return (f'Passengers:\n{passengers}\n'
                f'Drivers:\n{drivers}')