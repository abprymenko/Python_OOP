from student import Student
#1 One
illya = Student("Illya", 14.3, "S2813", 11.5)
#print(illya.Show())#AttributeError: 'Student' object has no attribute 'Show'
print(illya.__bool__())
print(illya.__len__())
print(illya)

#2 Many
anton = Student("Anton", 14, "S2813", 10)
andrii = Student("Andrii", 12, "S2813", 12)
radomyr = Student("Radomyr", 11, "S2813", 11.5)
kyrylo = Student("Kyrylo", 12, "S2813", 10.5)
ivan = Student("Ivan", 12, "S2813", 11)

students = list()
students.append(anton)
students.append(andrii)
students.append(radomyr)
students.append(kyrylo)
students.append(ivan)

for student in students:
    print(student)