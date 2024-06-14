
# Defining Functions
# • Function syntax and parameters
# • Return values
# • Lambda functions

'''
    Creating a Function
In Python a function is defined using the def keyword:
'''

def my_function():
    print("Hi there Allan!")
 
my_function()

#  Example 1:
def multiply(a, b):
    return a*b

result = multiply(5,7)

print(result)

# Example 2: return multiple  values

def get_cordinates():
    return 10, 20

x, y = get_cordinates()

print(x, y)

# Exercise 1: Define a function greet() with 
# a parameter name, set to 'Guest' and print a message
# I am a software programmer

def greet(name='Guest'):
    print(f"Hello, {name}!, I am a software programmer")

greet()        # This will use the default value 'Guest'
greet('Allan') # This will use 'Allan' as the name

# Example 3: return multiple  values

def get_name_and_position():
    name = 'Allan Edith, '
    position = 'I am a software programmer'

    return name, position

name, position = get_name_and_position()

print(name, position)

# Exercise 2: Return multiple values of your name and age

def get_name_and_age():
    name = 'Allan Edith, '
    age = 24

    return name, age

name, age = get_name_and_age()

print(name, age)

''' 
Lambda
Lambda functions in Python, also known as anonymous 
functions, are small, unnamed functions defined using the 
lambda keyword. They can have any number of arguments but only one expression.
'''

# syntax
# lambda arguments : expression

# Example 4: Create a lambda function to add two numbers

x = lambda a, b: a + b

print(x(2,5))

def add(a, b): return a * b

print(add(2, 7))

# Example 5: Use cases of lambda function for sorting
# Using Lambda with sorted()
# The sorted() function sorts a list. You can use a lambda function to specify a custom sort key.


coordinates = [(1,2), (2,3), (3,1), (5,0)]

coordinates.sort(key=lambda coordinate: coordinate[1])

print(coordinates)

# Example 6: Map, filter and Reduce. 
# Get the squares of 1 to 5 using map, filter and reduce

# Using Lambda with map()
# The map() function applies a given function to all items in an input list.

number_squares = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, number_squares))

print(squares)

'''
Or

numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))
'''

# Using Lambda with filter()
# The filter() function filters items out of a list based on a given condition.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = filter(lambda x: x % 2 == 0, numbers)

print(list(evens))  # Output: [2, 4, 6, 8, 10]

# Exercise 3: Define a function to get user info that accepts
#  arbitrary keyword arguments and print each key value pair

def get_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

get_user_info(name="Edith", age=25, occupation="Statistician")