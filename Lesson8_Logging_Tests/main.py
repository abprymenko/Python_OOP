from logging import *
from Lesson7_Iterators_GENERATORS_CLOSURES_DECORATORS.decorator import Calculator
from logger import Logger
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
    logger.Log(ERROR, ex)
'''

#2 Tests
def Add(digit1, digit2):
    return digit1 + digit2
logger = Logger(DEBUG, 'loggingFile.log')

def Test_Add_R_4():
    try:
        assert Add(2, 2) == 5, 'wrong answer 5'
    except Exception as ex:
        logger.Log(ERROR, ex)
Test_Add_R_4()
'''
try:
    assert Add(2, 2) == 5, 'wrong answer 5'
except Exception as ex:
    logger.Log(ERROR, ex)
try:
    assert Add(2, 2) == 6, 'wrong answer 6'
except Exception as ex:
    logger.Log(ERROR, ex)
try:
    assert Add(2, 2) == 0, 'wrong answer 0'
except Exception as ex:
    logger.Log(ERROR, ex)
'''
