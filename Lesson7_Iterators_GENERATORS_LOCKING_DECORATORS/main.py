from counter import Counter
from generator import Generator
from decorator import Checker
'''
students = [["Nikita", 15, True], 2, 3, 4, 5, "Andrii"]
iter_students = iter(students)
'''
#1
'''
iter_students1 = iter(students)
for student in iter_students:
    print(student)

for student in iter_students1:
    print(student)
'''
#2
'''
try:
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    #while(True):
        #print(next(iter_students))
        ##print(iter_students.__next__())
except StopIteration:
    pass
print("Hello Iterators")
'''
#3 Counter
'''
counter = Counter(25, 40)
try:
    while(True):
        print(next(counter))
except StopIteration:
    pass
'''
#4 Generator
'''
students = [["Nikita", 15, True], "Andrii", "Dima", "Roma", "Igor"]
generator = Generator(students)
for i in generator.GetStyudents():
    print(i)
'''
#5 Decorator
try:
    checker = Checker()
    digit1 = int(input("Enter digit1: "))
    digit2 = int(input("Enter digit2: "))
    operation = input("Select operation[/*-+]: ")
    checker.Calculate(f'{digit1}{operation}{digit2}')
except Exception as ex:
    print(ex)