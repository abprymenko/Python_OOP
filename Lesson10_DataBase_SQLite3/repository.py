import sqlite3
class Repository:
    def __init__(self, database:str, timeout:float):
        self.Database:str = database
        self.TimeOut:float = timeout
    def Query(self, sqlQuery:str):
        try:
            connection = sqlite3.connect(self.Database, self.TimeOut)
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            connection.commit()
        except Exception as ex:
            raise ex
        finally:
            connection.close()
    def QueryMany(self, sqlQuery:str, records: list):
        try:
            connection = sqlite3.connect(self.Database, self.TimeOut)
            cursor = connection.cursor()
            cursor.executemany(sqlQuery, records)
            connection.commit()
        except Exception as ex:
            raise ex
        finally:
            connection.close()
    def Execute(self, sqlQuery:str):
        try:
            connection = sqlite3.connect(self.Database, self.TimeOut)
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            return cursor.fetchall()
        except Exception as ex:
            raise ex
        finally:
            connection.close()

if __name__ == '__main__':
    repo = Repository('students.sl3', 5.0)
    # 1 CREATE TABLE ....(fields_definitions)
    '''
    repo.Query('CREATE TABLE S2813 (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20), age INT, avg_grade FLOAT)')
    '''

    # 2 INSERT INTO .... (name_of_fields) VALUES(set_of_values)
    # repo.Query("INSERT INTO S2813(name, age, avg_grade) VALUES('Akinin Illya', 14, 12)")
    # repo.Query("INSERT INTO S2813(name, age, avg_grade) VALUES('Gorobets Maksym', 14, 11.5)")
    # repo.Query("INSERT INTO S2813(name, age, avg_grade) VALUES('Protsko Arsenii', 13, 11)")
    # repo.Query("INSERT INTO S2813(name, age, avg_grade) VALUES('Klevaichuk Nikita', 15, 10.5)")

    # 3 Update .... SET ..... WHERE .....
    # repo.Query('UPDATE S2813 SET avg_grade=10.7 WHERE id = 2')
    # 4 DELETE FROM ... WHERE ....
    # repo.Query('DELETE FROM S2813 WHERE id=4')
    # 5 SELECT (set_name_of_fields) FROM ..... WHERE ...
    # res = repo.Execute('SELECT name, age FROM S2813 WHERE  avg_grade = 12')
    # print(res)
    # 6 DROP TABLE ....
    #repo.Query('DROP TABLE S2813')