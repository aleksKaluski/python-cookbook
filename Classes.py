
"""
CLASSES & OOP BASICS
"""

# ================================================================
# Creating a class
# ================================================================
class Person:
    species = "human"              # class attribute (shared)

    def __init__(self, name, age): # constructor
        self.name = name           # instance attribute
        self.age = age

    def greet(self):               # instance method
        return f"Hello, I'm {self.name}"


# ================================================================
# Creating an object (instance)
# ================================================================
p = Person("Alice", 20)
p.name
p.greet()


# ================================================================
# Class vs instance attributes
# ================================================================
Person.species        # accessed via class
p.species             # instance can access class attributes
p.name                # instance attribute, unique for each object


# ================================================================
# Methods
# ================================================================
class Example:
    def method(self):     # instance method (most common)
        return "instance"

    @classmethod
    def cmethod(cls):     # class method
        return "class"

    @staticmethod
    def smethod():        # static method (no access to class/instance)
        return "static"


# ================================================================
# Inheritance
# ================================================================
class Animal:
    def speak(self):
        return "?"

class Dog(Animal):        # Dog inherits from Animal
    def speak(self):
        return "Woof!"    # override method


d = Dog()
d.speak()                 # "Woof!"


# ================================================================
# super() — call parent methods
# ================================================================
class A:
    def say(self):
        return "A"

class B(A):
    def say(self):
        return "B" + super().say()

B().say()                 # "BA"


# ================================================================
# __str__ and __repr__
# ================================================================
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

# repr() → developer-friendly
# str() → user-friendly


# ================================================================
# Operator overloading
# ================================================================
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):      # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

