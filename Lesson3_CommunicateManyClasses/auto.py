from humanrole import HumanRole
from autotype import AutoType
from human import Human
class Auto:
    def __init__(self, model:str, type:AutoType):
        self.Model:str = model
        self.Type:AutoType = type
        self.Passengers:list = list()
        self.Drivers:list = list()
    def add_passengers(self, human:Human):
        if isinstance(self.Drivers, list) 
            and isinstance(human, Human)
            and human.Role == HumanRole.PASSENGER:
            self.Passengers.append(human)
    def add_drivers(self, human:Human):
        if isinstance(self.Drivers, list) 
            and isinstance(human, Human)
            and human.Role == HumanRole.DRIVER:
            self.Drivers.append(human)

    def __str__(self):
        #drivers = '\n'.join(str(driver) for driver in self.Drivers)
        #passengers = '\n'.join(str(passenger) for passenger in self.Passengers)
        drivers: str = ''
        passengers: str = ''
        for driver in self.Drivers:
            drivers += str(driver)
        for passenger in self.Passengers:
            passengers += str(passenger)
        return (f'Drivers:\n{drivers}\n'
                f'Passengers:\n{passengers}')