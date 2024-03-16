from human import Human


class Student(Human):
    def __init__(self, name: str, age: float, group: str, role: str):
        super().__init__(name, age, role)
        self.Group: str = group

    def __str__(self):
        return (f"Name: {self.Name}\n"
                f"Age: {self.Age}\n"
                f"Group: {self.Group}\n"
                f"Role: {self.Role}")
