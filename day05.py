print("hello world")

class Point:
    def new(self):
        print("hello rafi")
    
    def another(self):
        print("hello bappy")

var = Point()
var.new()

class Number:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def one(self):
        print("tis is one")

    def two(self):
        print("this is two")

var = Number(10, 20)
print(var.x, var.y)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("hellllo")


var = Person(name)
var.talk()

class Animal:
    def dog(self):
        print("this is a dog")

    
class Bird(Animal):
    pass

class Fish(Bird):
    pass

var = Bird()
var.dog()



