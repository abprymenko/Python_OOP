from iteratorcounter import Counter
from generator import Generator
from callobject import Helper
from decorator import Calculator

'''
students = [["Nikita", 15, True], 2, 3, 4, 5, "Andrii"]
iter_students = iter(students)
'''
#1 what is iterable objects?
'''
iter_students1 = iter(students)
for student in iter_students:
    print(student)

for student in iter_students1:
    print(student)
'''
#2 __next__()
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
#3 Iterator -> Counter
'''
counter = Counter(25, 40)
try:
    while(True):
        print(next(counter))
except StopIteration:
    pass
'''
#4 Generator :: yield
'''
students = [["Nikita", 15, True], "Andrii", "Dima", "Roma", "Igor"]
generator = Generator(students)
for i in generator.GetStyudents():
    print(i)
'''
#5 Closures
'''
def HelperFunc(work):
    #Data Encapsulation: Closures provide a way to encapsulate data within a function, limiting its visibility and accessibility from outside.
    work_in_memory = work
    def HelperInnerFunction(work):
        return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"
    return HelperInnerFunction
#stores pointer to HelperInnerFunction()
helper = HelperFunc("homework")#<function HelperFunc.<locals>.HelperInnerFunction at 0x00000230E2FA4B80>
print(helper("cleaning"))# f"I will help you with your homework. Afterwards I will help you with cleaning"
print(helper("driving"))# f"I will help you with your homework. Afterwards I will help you with driving"
'''
#5 Closures :: __call__(param) objects
'''
helper = Helper("homework")
print(helper("cleaning"))
print(helper("driving"))
'''
#6 Decorator
'''
try:
    calculator = Calculator()
    digit1 = int(input("Enter digit1: "))
    digit2 = int(input("Enter digit2: "))
    operation = input("Select operation[/*-+]: ")
    res = calculator.Calculate(f'{digit1}{operation}{digit2}')
    print(res)
    print("No exception")
except Exception as ex:
    print(ex)
'''