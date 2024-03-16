from auto import Human
from auto import Auto
from auto import AutoType
from auto import HumanRole

humans = list()
yasin = Human('Yasin', HumanRole.DRIVER)
nikita = Human('Nikita', HumanRole.PASSENGER)
illya = Human('Illya', HumanRole.PASSENGER)
arsenii = Human('Arsenii', HumanRole.PASSENGER)
for human in yasin, nikita, illya, arsenii:
    humans.append(human)

bmw = Auto("X7", AutoType.CAR)
for human in humans:
    bmw.add_passengers(human)
    bmw.add_drivers(human)
print(bmw)
'''
for driver in bmw.Drivers:
    print(driver)
for passenger in bmw.Passengers:
    print(passenger)
'''
