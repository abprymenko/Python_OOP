#1
'''
try:
    block_try_code
except type_exception:
    block_handle_code
finally:
    block_finally_code
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
from validator import *
from parser import *
limit = 10
amount = None
while True:
    try:
        amountStr = input("Enter amount: ")
        amount = Parser.NumericTryParse(amountStr)
        Validator.Check(amount, limit)
        print('Thanks for the purchase.')
    except Exception as ex:
        print(ex)
    finally:
        yes = input('Would you like try again?[Y/N]: ')
        if  yes.lower() != 'y':
            break
print("Welcome again.")
'''
#3 Warnings
'''
import warnings
warnings.simplefilter("ignore", SyntaxWarning)
#warnings.simplefilter("always", ImportWarning)
warnings.simplefilter("error", ImportWarning)
warnings.warn("Warning, no code here!", SyntaxWarning)
warnings.warn("Warning, module not import!", ImportWarning)
'''