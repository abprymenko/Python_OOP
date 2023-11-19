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
'''

def ShowMenu():
    for link in links:
        if link[2].lower() == 'nbu':
            print(f'[{link[0]} to buy currency.]')
        if link[2].lower() == 'weather':
            print(f'[{link[0]} to see the weather in Kyiv.]: \t')
def ValidateEnteredData(operation: str):
    while (not operation.isdigit()):
        ShowMenu()
        operation = input()
    return operation
def GetLink(links: list, value: int):
    for link in links:
        if(link[0] == value):
            return link[1]

links = repo.Execute('SELECT * FROM LINKS')
print('Select operation.\nEnter:')
operation = ValidateEnteredData('')
value = int(operation)
link = GetLink(links, value)
if value == 1:
    try:
        selectedCurrency = int(input("Select currency: \n[EU - 1]\n[USD - 2]: "))
        amount = float(input("Enter amount in hrn: "))
        parser = HtmlParser(link)
        parser.NbuParse('div', 'index-page')
        resDB: str
        if selectedCurrency == 1:
            symbol = "€"
            result = amount / parser.Result[2]
            resDB = f"amount - {amount} hrn; price - {parser.Result[2]} {symbol};result - {result:.2f} {symbol}"
        else:
            symbol = "$"
            result = amount / parser.Result[3]
            resDB = f"amount - {amount} hrn; price - {parser.Result[3]} {symbol};result - {result:.2f} {symbol}"
        repo.Query(f"INSERT INTO RESULT (result) VALUES('{resDB}')")
    except Exception as ex:
        print(ex)
elif value == 2:
    try:
        parser = HtmlParser(link)
        parser.WeatherParse('temperature')
        query = f"INSERT INTO RESULT(result) VALUES('{parser.Result[0]}')"
        repo.Query(query)
    except Exception as ex:
        print(ex)
else:
    print("no implementation")