from cat import Cat
from dog import Dog

murchyk = Cat(nick="Murchyk", age=1.2, breed="Siamese", sound="Meow-meow")
rokki = Dog(nick="Rokki", age=2.3, breed="German shepherd", sound="Woof-woof")
print(murchyk)
print(murchyk.Speak())
#print(murchyk.length)#
#print(murchyk._color)#
#print(murchyk.__eyescolor)#
print(rokki)
print(rokki.Speak())