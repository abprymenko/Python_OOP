#1 Create DB
from Lesson10_DataBase_SQLite3 import Repository
from Lesson9_WORK_WITH_SITES import HtmlParser
database = '../Files/exam.sl3'
timeout = 10.0

repo = Repository(database, timeout)
# 1.1 CREATE TABLE ....(fields_definitions)
'''
repo.Query('CREATE TABLE LINKS (id INTEGER PRIMARY KEY AUTOINCREMENT, link VARCHAR(50), name VARCHAR(20))')
repo.Query('CREATE TABLE RESULT (id INTEGER PRIMARY KEY AUTOINCREMENT, result VARCHAR(50))')
'''
# 2 INSERT INTO .... (name_of_fields) VALUES(set_of_values)
'''
records = [
    ('https://bank.gov.ua/', 'nbu'),
    ('https://meteo.ua/ua/34/kiev', 'weather')
]
query = "INSERT INTO LINKS (link, name) VALUES(?, ?)"
repo.QueryMany(query, records)
'''
res = repo.Execute('SELECT link FROM LINKS WHERE  id = 1')
parser = HtmlParser(res[0][0])
parser.NbuParse('div', 'index-page')
hrn = 1000
result = hrn/parser.Result['3']
rate = parser.Result['3']
rDb = f'{result:.2f}'
resDB = f'Exchange rate ={rate}, Hrn={hrn}, Result={rDb}'
query = f"INSERT INTO RESULT (result) VALUES('{resDB}')"
repo.Query(query)