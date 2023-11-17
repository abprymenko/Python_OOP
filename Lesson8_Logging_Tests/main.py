from logging import *
from Lesson8_Logging_Tests.calcmanager import CalcManager
from logger import Logger
import inspect

'''
debug("debug message")
info("info message")
warning("warning message")
error("error message")
critical("critical message")
'''

#1 Logger
'''
logger = Logger(DEBUG, 'loggingFile.log')
try:
    calculator = Calculator()
    digit1 = int(input("Enter digit1: "))
    digit2 = int(input("Enter digit2: "))
    operation = input("Select operation[/*-+]: ")
    res = calculator.Calculate(f'{digit1}{operation}{digit2}')
except Exception as ex:
    logger.Log(ex, ERROR)
'''

#2 Tests
loggerName = __name__
logger = Logger(loggerName, level=ERROR)
def Test_Add_R_4():
    try:
        #assert CalcManager.Add(2, 2) == 5, 'wrong answer 5'
        #assert CalcManager.Add(2, 2) == 6, 'wrong answer 6'
        #assert CalcManager.Add(2, 2) == 0, 'wrong answer 0'
        #assert CalcManager.Div(2, 0) == 0, "wrong answer 0"
        assert CalcManager.Div(2, 1) == 0, "wrong answer 0"
    except:
        raise
try:
    Test_Add_R_4()
except Exception as ex:
    #print(ex)
    try:
        logger.Log(ex)
    except Exception as ex:
        print(ex)
#3 doctest see in Lesson8_Logging_Testing.calcmanager.py file
#4 Unit tests in Lesson8_Logging_Testing.unittestsexample.py file