from  humanrole import HumanRole
class Human:
    def __init__(self, name:str, role:HumanRole):
        self.Name:str = name
        self.Role:HumanRole = role

    def __str__(self):
        return (f'Name - {self.Name}\n'
                f'Role - {self.Role.name}')
