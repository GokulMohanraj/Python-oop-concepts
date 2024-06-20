# class
# Creating a new class


class Hello:
    Word = "Welcome"

greeting = Hello()
print (greeting.Word)

# class with __init__ method:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("john", 23)

print (p1.name)
print (p1.age)

# class with __str__ method:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person name is {self.name} and age is {self.age}"

p1 = Person("john", 23)

print (p1)

# Object method

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"Hello my name is {self.name}")

p = Person("Wills", 23)
p.intro()

# Inheritance method:

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# parent class

class person():
    def __init__(self,fname, lname):
        self.firstName = fname
        self.lastName = lname

    def printName(self):
        print(self.firstName, self.lastName)

x = person("Will", "Jack")
x.printName()

# Child Class (or) derived class

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationYear = year

    def Welcome(self):
        print("Welcome", self.firstName, self.lastName, "to the class of", self.graduationYear)

x = student("Will", "Jack", 2019)
x.Welcome()

# Polymorphism 
# polymorphism means many forms, and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

class car():
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def move(self):
        print("Driving...!")

class plane():
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def move(self):
        print("Flying...!")

car1 = car("Tata", 2019)
plane1 = plane("Airline", 2011)

for x in (car1, plane1):
    x.move()

# Inheritance in polymorphism :

class vehicle():
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def move(self):
        print("Moving...!")

class car(vehicle):
    pass

class plane(vehicle):
    def __init__(self, name, model):
        super().__init__(name, model)

    def move(self):
        print("Flying...!")

car2 = car("Suzuki", 2020)
plane2 = plane("Express", 2016)

for x in (car2, plane2):
    print(x.name)
    print(x.model)
    x.move()


# Encapsulation 
# It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.

class car():
    # This is a public function 

    def open_door_and_preform(self):
        print("opening door..!")
        self._accelerate()

    # This is a protected function

    def _accelerate(self):
        print("accelerating..!")
        self.__engine_performing()

    # This is a private function

    def __engine_performing(self):
        print("engine performing..!")
        print("Car moving..!")


myCar = car()
myCar.open_door_and_preform()