


# ITERATORS

# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.


myset = {"apple", "banana", "cherry"}

myiter = iter(myset)

print(next(myiter))
print(next(myiter))
print(next(myiter))

mystr = "Banana"

myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# We can also use a for loop to iterate through an iterable object:

for x in myset:
    print(x)

for x in mystr:
    print(x)






# JSON IN PYTHON

# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.

# Python has a built-in package called json, which can be used to work with JSON data.

# Import the json module:

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

import json

# some JSON:
x =  '{"name":"Ocung", "age":24, "city":"Soroti"}'

# print(x["age"])

y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

z = {
  "name": "Allan",
  "age": 23,
  "city": "Soroti"
}

# convert into JSON:
w = json.dumps(z)

# the result is a JSON string:
print(w)








# PIP

# PIP is a package manager for Python packages.
# If you have Python version 3.4 or later, PIP is included by default.

# What is a Package?
# A package contains all the files you need for a module.
# Modules are Python code libraries you can include in your project.

# To check if PIP is installed: py -m pip --version

# PIP commands

# Download a Package
# Navigate your command line to the location of Python's script directory, and type the following:

# e.g C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase

# Import the "camelcase" package into your project.

import camelcase

c = camelcase.CamelCase()

txt = "Modules are Python code libraries you can include in your project"

print(c.hump(txt))

# To list the installed packages:   C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip show package_name
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase