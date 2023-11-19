import unittest
from calcmanager import CalcManager
from logger import Logger
import inspect
from logging import ERROR
class UseUnitTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(UseUnitTests, self).__init__(*args, **kwargs)
        self.__Setup()

    def __Setup(self):
        frame = inspect.currentframe()
        try:
            calling_class = frame.f_back.f_locals.get('self', None)
            loggerName: str = calling_class.__class__.__name__ if calling_class is not None else None
            self.__Logger = Logger(loggerName, level=ERROR)
        except:
                raise
        finally:
            del frame
    def test_args1(self):
        try:
            self.assertEqual(CalcManager.AddArgsKWArgs(2, 2), 4)
        except Exception as ex:
            try:
                self.__Logger.Log(ex)
            except:
                raise

    def test_args2(self):
        try:
            self.assertEqual(CalcManager.AddArgsKWArgs(2, 3), 4)
        except Exception as ex:
            try:
                self.__Logger.Log(ex)
            except:
                raise
    def test_args3(self):
        try:
            self.assertEqual(CalcManager.AddArgsKWArgs(-2, 3), 4)
        except Exception as ex:
            try:
                self.__Logger.Log(ex)
            except:
                raise

if __name__ =="__main__":
    unittest.main()