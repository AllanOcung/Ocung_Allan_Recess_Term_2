# Dictionaries
# Creating and using dictionaries
# Dictionary methods and operations

# Example 1: 
# Create a dictionary for a student pursuing software 
# engineering, the key must be your name, age, 
# technology interest andyear of study. put your own details

student = {
    "name" : "Edith", 
    "age": 35, 
    "technology_interest" : "Artificial Intelligence", 
    "year_of_study" : 3

    }

print(student["name"])
print(student["age"])
print(student["technology_interest"])
print(student["year_of_study"])

# Modify values

# Exercise 1: 
# Modify age and technology interest

student["age"] = 37
student["technology_interest"] = "Machine Learning"

print(student)

# Example 2: Adding keys and values

student["email"] = "allansocung137@gmail.com"

print(student)

# Exercise 2:
# Remove a key and value from the dictionary

# student.pop("name")

# del student["age"]

# print(student)



# Common Dictionary methods
"""summary
get() // returns the value for the specified key if the key is in the dictionary
if not it returns the default value

update() // Updates the dictionary with the elements from another dictionary

pop() // Removes the specified key and return the corresponding value



"""
# Example 3: Use the get method to get the value

print(student.get('technology_interest'))

# Exercise 3: Use the update method to change value in age 

student.update({'age': '25'})
print(student)
print()

# Exercise 4: Use the if to check if the key 'age' is present in the dictionary

if 'age' in student:
    print(" age is present in the dictionary.", student['age'])
    
else:
    print(" age is not present in the dictionary.")
    
print()

# keys(), values() and the items() methods
print(student.keys())
print(student.values())
print(student.items())

"""summary

keys() returns a view of objects that displays a list of all keys
values() returns a view of objects that displays a list of all values
items() returns a view of objects that displays a list of dictionary keys and
values tuple pairs

 """
 
 # Exercise : Use the update method to change the course and add a new 
 # key "WhatsApp_Number" to the dictionary
 
student.update({
    'course': 'BSSE',
    'WhatsApp_Number': '0771895380'
})
print(student)
print()