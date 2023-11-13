from student import Student
illya = Student("Illya", 14.3, "S2813", 11.5)
#print(illya.Show())#AttributeError: 'Student' object has no attribute 'Show'
print(illya.__bool__())
print(illya.__len__())
print(illya)