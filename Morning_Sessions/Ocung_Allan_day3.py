# https://docs.google.com/forms/d/e/1FAIpQLSc_QswLYhvuV-RS6GpIea42b1fg-mE2L0vZQoZrplMpNowsDQ/viewform?fbzx=4194617982376852790

#comprehensions (ist, dictionary comprehensions)
"""
comprehensions provide a concise way to create lists and dictionaries
"""
#Example 1
#Create a list of squares in range of 10

squares = [x**2 for x in range(10)]

print(squares)

#Exercise 2
#create a list of even squares in the range of 20

list_of_even_squares = [k**2 for k in  range(20) if k % 2 == 0]
print(list_of_even_squares)

'''
Create a list containing your favouite cars. 
then use dictionary comprehension to create a dictionary where the 
keys are the car names and the values are the lengths of those car names 
(i.e., the number of characters in each car name). 
'''

favouriteCars = ['Toyota Camry', 'Honda Accord', 'Audi A4', 'Tesla Model S']

car_length = {car: len(car) for car in favouriteCars}

print(car_length)

#Create a list of tuples where each tuple contains a number and its cube for numbers between 1 and 10 using a 
#dictionary comprehension

cubes = [(x, x**3) for x in range(1, 11)]

print(cubes)