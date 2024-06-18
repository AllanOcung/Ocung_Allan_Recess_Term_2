
print()
print("-----------------Classes and Objects-------------------")
print()

# Classes and Objects
'''
class MyClass: # Creating a class
    x = 7

p1 = MyClass() # Creating an object

print(f"The value of x is {p1.x}")

'''

class Dog:
    # class attribute
    species = 'canis familiaris'

    # initializer / instance attriutes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    

my_dog = Dog("Buddy", 3) # Creating object

# Accessing attributes

print(my_dog.name)
print(my_dog.age)

print(my_dog.species)

# Modifying object properties

my_dog.name = 'Lucy'

print(my_dog.name)

# calling methods

print(my_dog.description())
print(my_dog.speak("woof woof"))

'''
The self parameter is a reference to the current instance of the class, 
and is used to access variables that belong to the class.

'''

# Deleting object properties

'''
del my_dog.name

print(my_dog.name)
'''

# Deleting an object

'''
del my_dog

print(my_dog.age) 
'''

print()
print("-----------------Inheritence-------------------")
print()
# Inheritence

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

x = Person('Akurut', 'Edith')

x.printname()


class Student(Person):
    # pass      # Use the pass keyword when you do not want to add any other properties or methods to the class.

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname) # Person.__init__(self, fname, lname)
        self.graduationYear = year
    
    def welcome(self):
        print(f"Welcome, {self.fname} {self.lname} to the class of {self.graduationYear}")

y = Student('Allan', 'Ocung', 2023)

print(y.graduationYear)

y.printname()

y.welcome()



print()



class Bulldog(Person):
    def run(self, speed):
        print(f"{self.fname} runs very {speed}")


z = Bulldog('Olsen', 'Mike')

z.printname()

print(z.run('fast'))


print()

print()
print("-----------------Polymorphism-------------------")
print()

# Polymorphism

# Class Polymorphism

'''
Polymorphism is often used in Class methods, where we can 
have multiple classes with the same method name.
'''
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('drive!')


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Sail!')

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Fly!')


car1 = Car("Ford", "Mustang")

boat1 = Boat("Ibiza", "Touring 20")

plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()
