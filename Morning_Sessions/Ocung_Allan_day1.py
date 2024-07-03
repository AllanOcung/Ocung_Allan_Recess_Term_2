
import sys

print(sys.version)  # Checking for python version

print()

print("Hello, World!")

print()

# Python Syntax

# Python Indentation
# Indentation refers to the spaces at the beginning of a code line.

# Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

# Python uses indentation to indicate a block of code.

if 5 > 2:
  print("Ten is greater than Five!")


# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
print()

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 


print()
# Python Variables
# In Python, variables are created when you assign a value to it:

x = 5
y = "John"
print(x)
print(y)

# Comments
"""
This is a comment
written in
more than just one line
"""

# Casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the Type
# You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))


# Case-Sensitive
# Variable names are case-sensitive.

# This will create two variables:

a = 4
A = "Sally"
#A will not overwrite a

print(a)
print(A)

print()

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print()

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

print()

# Global Variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Python Data Types
# Built-in Data Types
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''