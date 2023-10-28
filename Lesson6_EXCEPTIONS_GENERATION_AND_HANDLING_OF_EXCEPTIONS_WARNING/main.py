#1
'''
try:
    block_code
except type_exception:
    block
'''
'''
try:
    digit1 = int(input("Enter digit: "))
    digit2 = int(input("Enter digit: "))
    print(digit1/digit2)
except ValueError as ve:
    print(f'[ValueError]: {ve}')
except ZeroDivisionError as zde:
    print(f'[ZeroDivisionError]: {zde}')
except Exception as ex:
    print(f'[Exception]: {ex}')
print("Hello world")
'''
#2
'''
from builterror import BuildError
from validation import Validator
limit = 10
amountStr = input("Enter amount: ")
amount = None
validator = Validator()
try:
    while(True):
        if(amountStr.isdigit()):
            amount = int(amountStr)
            break
        amountStr = input("Enter amount as integer digit: ")
    validator.Check(amount, limit)
except BuildError as be:
    print(be)
except Exception as ex:
    print(ex)
print('Hello world')
'''
#3 Warnings
import warnings
warnings.simplefilter("ignore", SyntaxWarning)
#warnings.simplefilter("always", ImportWarning)
warnings.simplefilter("error", ImportWarning)
warnings.warn("Warning, no code here!", SyntaxWarning)
warnings.warn("Warning, module not import!", ImportWarning)

