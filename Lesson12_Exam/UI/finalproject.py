from Lesson10_DataBase_SQLite3 import Repository
from Lesson9_WORK_WITH_SITES import HtmlParser
class UserInterface:
    def ShowMenu(self, links: list):
        for link in links:
            if link[2].lower() == 'nbu':
                print(f'[{link[0]} to buy currency.]')
            if link[2].lower() == 'weather':
                print(f'[{link[0]} to see the weather in Kyiv.]: \t')
    def ValidateEnteredData(self, operation: str, links: list):
        while (not operation.isdigit()):
            self.ShowMenu(links)
            operation = input()
        return operation
    def GetLink(self, links: list, value: int):
        for link in links:
            if (link[0] == value):
                return link[1]
    def CurrencyExangeProcess(self, link: str, repo: Repository):
        try:
            selectedCurrency = int(input("Select currency: \n[EU - 1]\n[USD - 2]: "))
            amount = float(input("Enter amount in hrn: "))
            parser = HtmlParser(link)
            parser.NbuParse('div', 'index-page')
            rate: float
            symbol: str
            if selectedCurrency == 1:
                symbol = "€"
                rate = parser.Result[2]
            else:
                symbol = "$"
                rate = parser.Result[3]
            result = amount / rate
            resDB = f"amount - {amount} hrn; price - {rate} {symbol}; result - {result:.2f} {symbol}"
            query = f"INSERT INTO RESULT (result) VALUES('{resDB}')"
            repo.Query(query)
            print(resDB)
        except:
            raise
    def WeatherProcess(self, link: str, repo: Repository):
        try:
            parser = HtmlParser(link)
            parser.WeatherParse('temperature')
            query = f"INSERT INTO RESULT(result) VALUES('{parser.Result[0]}')"
            repo.Query(query)
            print(parser.Result[0])
        except:
            raise

if __name__ == '__main__':
    database = '../Files/exam.sl3'
    timeout = 10.0
    repo = Repository(database, timeout)
    #1 Create DB => create file exam.sl3
    #2 CREATE TABLE ....(fields_definitions)
    '''
    repo.Query('CREATE TABLE LINKS (id INTEGER PRIMARY KEY AUTOINCREMENT, link VARCHAR(50), name VARCHAR(20))')
    repo.Query('CREATE TABLE RESULT (id INTEGER PRIMARY KEY AUTOINCREMENT, result VARCHAR(50))')
    '''
    #3 INSERT INTO .... (name_of_fields) VALUES(set_of_values)
    '''
    records = [
        ('https://bank.gov.ua/', 'nbu'),
        ('https://meteo.ua/ua/34/kiev', 'weather')
    ]
    query = "INSERT INTO LINKS (link, name) VALUES(?, ?)"
    repo.QueryMany(query, records)
    '''
    #4 APP
    ui = UserInterface()
    links = repo.Execute('SELECT * FROM LINKS')
    print('Select operation.\nEnter:')
    operation = ui.ValidateEnteredData('', links)
    value = int(operation)
    link = ui.GetLink(links, value)
    if value == 1:
        try:
            ui.CurrencyExangeProcess(link, repo)
        except Exception as ex:
            print(ex)
    elif value == 2:
        try:
            ui.WeatherProcess(link, repo)
        except Exception as ex:
            print(ex)
    else:
        print("no implementation")