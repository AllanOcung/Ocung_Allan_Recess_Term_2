
'''
We can use the module we created by using the 'import' statement
'''

# Import the module named mymodule, and call the greeting function
import mymodule as mx

mx.greeting('Allan')


# Import the module named mymodule, and access the person1 dictionary

age = mx.person['age']

print(age)

# Import From Module
'''
You can choose to import only parts from a module, by using the from keyword
'''

# Example
# Import only the person dictionary from the module:

from mymodule import person

print(person['name'])

'''
Note: 
When importing using the from keyword, do not use the module name when referring 
to elements in the module. Example: person1["age"], not mymodule.person1["age"]
'''