from teacher import Teacher
from student import Student
andrii = Teacher("Andrii", 36.10, "PythonOOP", "teacher")
yaroslav = Student("Yaroslav", 12.08, "SP2122", "student")
oleksandr = Student("Oleksandr", 14.02, "SP2122", "student")
denys = Student("Denys", 12.06, "SP2122", "student")
dmytro = Student("Dmytro", 12.03, "SP2122", "student")
kyrylo = Student("Kyrylo", 14.01, "SP2122", "student")
humans = list()
for human in andrii, yaroslav, oleksandr, denys, dmytro, kyrylo:
    humans.append(human)
for human in humans:
    print(human)