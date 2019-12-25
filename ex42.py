####

class Animal(object):
    pass

class Dog(Animal):
    """This is a Dog class"""

    def __init__(self, name):
        """ Takes in self and name """
        """ Dog has an attribute name"""
        self.name = name

class Cat(Animal):

    """Making a new Cat class with cat names"""


    def __init__(self, name):
        """Creating the name property for a Cat class with is inherited from Animal class"""
        self.name = name

class Person(object):
    """creating a new class for person"""
    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):
    """creating a new class inhertiing from Person superclass"""

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

##creating a new class of fish
class Fish(object):
    pass

##Salomn is-a type of fish
class Salmon(Fish):
    pass

###Hailbut is-a type of fish 
class Halibut(Fish):
    pass


##now creating instances of classes above
rover = Dog("Rover")

satan = Cat("satan")

mary = Person("Mary")

mary.pet = satan

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()