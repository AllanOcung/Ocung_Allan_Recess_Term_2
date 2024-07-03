# Javascript: React
# php: Laravel
# laracust / making my own framework






# Inheritance and Polymorphism

'''
Inheritance and method overriding
Polynorphism and method resolution order
Abstract classes and interfaces

'''
# Example 1: Syntax

class Animal:
    def speak(self):
        return 'Mooo'


class Dog(Animal):
    def speak(self):
        return 'woof woof'
    

animal = Animal()

print(f"Animal: {animal.speak()}")

dog = Dog()

print(f"Dog: {dog.speak()}")



# Example 2: Polymorphism


class Vehicle:
    def sound(self):
        return 'wooof'

class Tesla(Vehicle):
    def sound(self):
        return 'vooommm'
    
class Mustang(Vehicle):
    def sound(self):
        return 'oooommmm'
    
def make_vehicle_sound(animal):
    print(animal.sound())

make_vehicle_sound(Tesla())
make_vehicle_sound(Mustang())

print()
print('Exercise 1: Solution')
print()

# Exercise 1:

'''
Create a simple application to manage different types of vehicles. Implement
inheritance and polymorphism.

Requirements:

1. Base class to vehicle
    Attributes: make, model, year
    Methods: display_info()

2. Derived classes

    Car: inherite from vehicle
        Attributes: number_of_doors
        overrides: display_info()

    Motorcycle: inherite from vehicle
        Attributes: type_of_bike(cruiser, sport, touring)
        overrides: display_info()

'''

# Solutio to Exercise 1:

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"Vehicle Info: {self.year} {self.make} {self.model}"
    

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        return f"Car Info: {self.year} {self.make} {self.model}, Doors: {self.number_of_doors}"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        return f"Motorcycle Info: {self.year} {self.make} {self.model}, Type: {self.type_of_bike}"

# # Create instances of Car and Motorcycle

car = Car('Toyota', 'Corolla', 2023, 4)

motorcycle = Motorcycle('Harley-Davidson', 'Street 750', 2019, 'Cruiser')

# Display info

print(car.display_info())

print()

print(motorcycle.display_info())

print()
print('Exercise 2: Solution')
print()


# Exercise 2:

'''
Create a function that accepts a list of vehicle objects and call their display_info()
method tp print details of each vehicle.

'''
# Solution

def print_vehicle_details(vehicles):
    for vehicle in vehicles:
        print(vehicle.display_info())


# Create instances of Car and Motorcycle

car1 = Car("Toyota", "Corolla", 2020, 4)

car2 = Car("Honda", "Civic", 2021, 2)

motorcycle1 = Motorcycle("Harley-Davidson", "Street 750", 2019, "Cruiser")

motorcycle2 = Motorcycle("Yamaha", "YZF-R1", 2022, "Sport")

# List of vehicle objects

vehicles = [car1, car2, motorcycle1, motorcycle2]

# Print details of each vehicle

print_vehicle_details(vehicles)

print()


# File Handling

print()
print('Working with text files')
print()

# Example 1: On file handling

# Writing to a text file

with open('edith.txt', 'w') as file:
    file.write('Edith is my mother and i love her so dearly. \n')
    file.write('She is so lovely')

# Reading from a text file

with open('edith.txt', 'r') as file:
    content = file.read()
    print(content)


print()
print('CSV Files')
print()

# Handling CSV files
'''
CSV (Comma Separated Values) file

It's widely used for data exchange

Read CSV files: Use 'csv.reader()'
Writing CSV files: Use 'csv.writer()'
DictReader and DictWriter: The class read and write CSV files as dictionaries

'''
# Example 2: On Writing and Reading CSV files

import csv

# writing to a csv file

with open('edith.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'position', 'passion'])
    writer.writerow(['Edith Akurut', 'Matron', 'God'])
    writer.writerow(['Allan Ocung', 'Son', 'IT'])

# Reading from a csv file

with open('edith.csv', 'r') as csv_file:        
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

print()
print('JSON and XML file processing')
print()

    
# JSON and XML file processing

'''
JSON (Javascript Object Notation)
XML (eXtensible Markup Language)
'''

# Example 3: Writing and reading JSON file

import json

student = {
    'name': 'Allan',
    'course': 'BSSE',
    'year': 2
}

with open('student.json', 'w') as json_file:
    json.dump(student, json_file)

with open('student.json', 'r') as json_file:
    student = json.load(json_file)
    print(student)

print()
print()

# Exercise 2: Write and read xml file

import xml.etree.ElementTree as ET

# Function to write to an XML file
def write_xml():
    # Create the root element
    root = ET.Element("data")

    # Create a child element
    item1 = ET.SubElement(root, "item")
    item1.set("name", "item1")
    item1.text = "This is item 1"

    # Create another child element
    item2 = ET.SubElement(root, "item")
    item2.set("name", "item2")
    item2.text = "This is item 2"

    # Create a tree object
    tree = ET.ElementTree(root)

    # Write the tree to an XML file
    tree.write("output.xml", encoding="utf-8", xml_declaration=True)
    print("XML file written successfully.")

# Function to read from an XML file
def read_xml():
    # Parse the XML file
    tree = ET.parse("output.xml")
    root = tree.getroot()

    # Iterate over the child elements
    for item in root.findall("item"):
        name = item.get("name")
        text = item.text
        print(f"Item name: {name}, Item text: {text}")

# Write XML
write_xml()

# Read XML
read_xml()

print()
print()


# Exercise 3: Using abstraction, calculatethe area and parameterof a rectangle

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

width = 5
height = 3 
rectangle = Rectangle(width, height)

print(f"Rectangle width: {rectangle.width}")
print(f"Rectangle height: {rectangle.height}")
print(f"Area of the rectangle: {rectangle.area()}")
print(f"Perimeter of the rectangle: {rectangle.perimeter()}")

