class Student:
    def __init__(self, name:str, age:float, group:str, avg_grade:float = None):
        self.Name:str = name
        self.Age:float = age
        self.Group:str = group
        self.Avg_Grade:float = avg_grade
    def __bool__(self):
        return self.Name != None and\
                self.Age != None and\
                self.Group != None and\
                self.Avg_Grade != None
    def __len__(self):
        return len(self.Name)
    def __str__(self):
        return (f"Name - {self.Name}\n"
                f"Age - {self.Age}\n"
                f"Group - {self.Group}\n"
                f"Avg_Grade - {self.Avg_Grade}")

if __name__ == "__main__":
    student = Student("Illya", 14.3, "S2813")
    print(student.__bool__())