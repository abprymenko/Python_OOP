'''
import requests
response = requests.get("https://httpbin.org/get")
print(response.status_code)
print(response.content)
'''

from htmlparser import HtmlParser
parser = HtmlParser("https://bank.gov.ua/")
parser.NbuParse('div', 'index-page')