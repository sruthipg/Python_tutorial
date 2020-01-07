class Animal(object):
    def __init__(self,name):
        self.name=name

    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print("Meow")

class Dog(Animal):
    def talk(self):
        print("Woof")

a = Animal("Test")
a.talk()

c=Cat("Test")
c.talk()

d=Dog("TestDog")
d.talk()
# Python implicitly polymorphic bz for access index tuples and list are same
# Hierarchical inheritance multiple children
# Animal is generic class
