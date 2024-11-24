'''
In Python, decorators are functions that allow us to modify or wrap another function or method,
adding additional behavior without changing its original code.
In OOP, they are often used for logging, access control, caching, etc.

### How it works:
- The `Log_Method_Call` decorator:
  - Wraps the Add and Subtract methods.
  - Adds logging for the method call and its result.

- Using the decorator:
  - The decorator is invoked when the method is marked with @.
  - @Log_Method_Call essentially wraps the add and subtract functions inside the wrapper function.

### Why it is needed:
- Code reuse: Decorators allow us to easily add behavior to many methods or functions.
- Code clarity: Our core logic remains unchanged, while additional functionality,
                such as logging, is implemented separately.
- Flexibility: We can easily modify or extend the behavior of classes without changing their code.
'''
from datetime import datetime

import datetime
def Log_Method_Call(method):
    def Wrapper(self, *args, **kwargs):
        print(f"[{datetime.datetime.now()}] Call the method:  '{method.__name__}' with arguments {args} і {kwargs}")
        result = method(self, *args, **kwargs)
        print(f"[{datetime.datetime.now()}] The method '{method.__name__}' returns {result}")
        return result
    return Wrapper


class Calculator:
    def __init__(self, value=0):
        self.value = value

    @Log_Method_Call
    def Add(self, number):
        self.value += number
        return self.value

    @Log_Method_Call
    def Subtract(self, number):
        self.value -= number
        return self.value


if __name__ == '__main__':
    calc = Calculator()
    calc.Add(10)  # It logs the calling of the method Add()
    calc.Subtract(5)  # It logs the calling of the method Subtract()

'''
[...datetime.datetime.now()...] Call the method:  'Add' with arguments (10,) і {}
[...datetime.datetime.now()...] The method 'Add' returns 10
[...datetime.datetime.now()...] Call the method:  'Subtract' with arguments (5,) і {}
[...datetime.datetime.now()...] The method 'Subtract' returns 5
'''