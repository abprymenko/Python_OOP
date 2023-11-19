import requests as r
from bs4 import BeautifulSoup as bs
import datetime

class HtmlParser:
    def __init__(self, url:str):
        self.Url:str = url
        self.Result:dict = {}

    def NbuParse(self, tag:str, attribute:str):
        try:
            response = r.get(self.Url)
            response_content = response.content
            html = bs(response_content, features="html.parser")
            tags = html.find_all(tag, attrs={'class': attribute})
            counter = 0
            for tag in tags:
                strValue = tag.text.strip().replace(',', '.')
                self.Result[counter] = float(strValue)
                counter += 1
        except:
            raise

    def WeatherParse(self, separator1: str):
        try:
            response = r.get(self.Url)
            response_content = response.content
            html = bs(response_content, features="html.parser")
            tags = html.find_all('div', attrs={'data-key': separator1})
            self.Result[0] = (f"date - {datetime.datetime.now().date()}\n"
                              f"temperature - {tags[0].text}")
        except:
            raise
if __name__ == '__main__':
    '''
    import requests
    response = requests.get("https://httpbin.org/get")
    print(response.status_code)
    print(response.content)
    '''

    parser = HtmlParser("https://bank.gov.ua/")
    parser.NbuParse('div', 'index-page')
    print(parser.Result)
    parser.Result = {}
    parser.Url = 'https://meteo.ua/ua/34/kiev'
    parser.WeatherParse('temperature')
    print(parser.Result)