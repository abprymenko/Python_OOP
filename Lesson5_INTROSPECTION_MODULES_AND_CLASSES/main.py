import requests
import colorama
#help(requests)
import inspect
'''
r = requests.get('https://www.python.org')
print(r.status_code)
print(r.content)
'''

'''
payload = dict(key1='group', key2='S2813')
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
'''

#print(requests.__name__)
#print(type(requests.Response()))
#print(dir(requests.Response))

'''
name = 'Andrii'
print(hasattr(name, 'reverse'))
print(hasattr(name, 'index'))
print(getattr(name, 'startswith1', "object has no attribute 'startswith1'"))

def get_full_name():
    pass
print(callable(name))
print(callable(get_full_name))
'''
'''
class Parent:
    pass
class Child(Parent):
    pass
class Auto:
    pass

bmw = Auto()
son = Child()
print(issubclass(Child, Parent))
print(issubclass(Auto, Parent))
print(isinstance(bmw, Auto))
print(isinstance(son, Auto))
print(isinstance(son, Parent))
print(isinstance(son, Child))
'''
#Inspect
def Hello():
    print("Hello Python")
def Age():
    return 17

class MyClass:
    def Hello(self):
        print("Hello Python")
    def Age(self):
        return 17
obj = MyClass()

#just functions
print(inspect.isfunction(Hello))#True
print(inspect.ismethod(Hello))#False
print(inspect.isfunction(Age))#True
print(inspect.ismethod(Age))#False
#obj -> MyClass
print(inspect.isfunction(obj.Hello))#False
print(inspect.ismethod(obj.Hello))#True
print(inspect.isfunction(obj.Age))#False
print(inspect.ismethod(obj.Age))#True

'''
print(inspect.ismodule(requests))
print(type(requests))
print(inspect.isclass(requests.Request))
print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))
'''

'''
help(colorama.Fore)
'''