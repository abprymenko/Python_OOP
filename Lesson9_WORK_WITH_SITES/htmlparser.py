import requests as r
from bs4 import BeautifulSoup as bs
class HtmlParser:
    def __init__(self, url:str):
        self.Url:str = url
        self.Result:dict = {}

    def NbuParse(self, tag:str, attribute:str):
        response = r.get(self.Url)
        response_content = response.content
        html = bs(response_content, features="html.parser")
        tags = html.find_all(tag, attrs={'class': attribute})
        counter = 0
        for tag in tags:
            try:
                strValue = tag.text.strip().replace(',', '.')
                self.Result[f'{counter}'] = float(strValue)
                counter += 1
            except Exception as ex:
                print(ex)