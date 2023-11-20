from sqlalchemy import ColumnElement
from dbcontext import DbContext
from student import Student


def GetStudents():
    eva = Student("Eva", 15, 12.0)
    uliana = Student("Uliana", 15, 12.0)
    bogdan = Student("Bogdan", 14, 12)
    mark = Student("Mark", 14, 12)
    saleh = Student("Magomed-Saleh", 13, 10)
    return [eva, uliana, bogdan, mark, saleh]

def CreateContext():
    url = 'sqlite:///itstep.db'
    return DbContext(url)
def SeedDB(context: DbContext):
    try:
        context.CreateTables()
        context.OpenSession()
        students = GetStudents()
        context.AddAll(students)
    except:
        raise
    finally:
        context.CloseSession()
def ShowAllStudents(context: DbContext, filter: ColumnElement[bool] = None):
    try:
        studentsDb = context.QueryAll(filter, Student)
        for student in studentsDb:
            print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Avg Grade: {student.avg_grade}")
    except:
        raise

if __name__ == '__main__':
    try:
        context = CreateContext()
        #SeedDB(context)
        context.OpenSession()
        filter = Student.age > 14
        ShowAllStudents(context, filter)
        context.AddInstance(Student( "Magomed-Emin", 14, 12))
        ShowAllStudents(context)
    except Exception as ex:
        print(ex)
    finally:
        context.CloseSession()
