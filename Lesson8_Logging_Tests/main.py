from logging import *
from Lesson8_Logging_Tests.calcmanager import CalcManager
from logger import Logger
from Lesson7_Iterators_GENERATORS_CLOSURES_DECORATORS.decorator import Calculator
import inspect
'''
loggerName = 'Lesson8_main'
logger = Logger(loggerName, 'loggingFile.log')
'''
'''
logger.Log("debug message", DEBUG)
logger.Log("info message", INFO)
logger.Log("warning message", WARN)
logger.Log("error message", ERROR)
logger.Log("critical message", FATAL)
'''
#1 Logger
'''
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
'''
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
        logger.Log(ex, ERROR)
    except Exception as ex:
        print(ex)
'''
#3 doctest see in Lesson8_Logging_Testing.calcmanager.py file
#4 Unit tests in Lesson8_Logging_Testing.unittestsexample.py file