class Person:
    def __init__(self, name, age):
        self.r = name
        self.i = age
    def __str__(self):
        return f"{self.r}: {self.i}"
    def func(self):
        print("My name is " + self.r)
    def hello(self):
        print("hello")
    def world(self):
        print("world")
        

x = Person("Anna", 24)
# del x.name #deletes name attribute of x instance of a class
x.func()
x.world()

# https://docs.python.org/3/tutorial/classes.html
# https://www.w3schools.com/python/python_classes.asp