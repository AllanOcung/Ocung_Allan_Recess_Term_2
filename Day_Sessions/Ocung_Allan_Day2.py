
# score = 85

# if score >= 90:
#     print("Excellent")

# elif score >= 80:
#     print("Very Good")

# elif score >= 70:
#     print("Good")

# elif score >= 60:
#     print("Well Tried")

# else:
#    print("You failed")


# EXERCISE 1:

# age = int(input("Enter your age: "))

# if age < 13:
#         print("Your Discount is: Shs1000")

# elif 13 <= age < 18:
#     print("Your Discount is: Shs500")

# elif 18 <= age < 60:
#     print("The price of the movie ticket is: Shs2000")

# else:
#     print("The price of the movie ticket is: Shs5000")


# LOOPS(for, while)

cars = [
    "Toyota Camry",
    "Honda Accord",
    "Ford Mustang",
    "Chevrolet Corvette",
    "Tesla Model S",
    "BMW 3 Series",
    "Audi A4",
    "Mercedes-Benz C-Class"
]
for x in cars:
    print(x)

x = 1

while x <= 10:
    print(x)
    x += 1
  
# EXERCISE 2

# 1. Create a list of your favourite colors using a for loop

color_names = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Black", "White"]

favourite_colors = []

for color in color_names:
    favourite_colors.append(color)
    print(color)

# 2. Create a reverse of the input 12345 to be 54321 using while loop

number = 12345

# Convert the number to a string to manipulate it easily
number_str = str(number)

# Initialize the reversed number as an empty string
reversed_number_str = ""

# Get the length of the number string
length = len(number_str)

# Initialize the index to the last character of the number string
index = length - 1

# Use a while loop to reverse the number string
while index >= 0:
    reversed_number_str += number_str[index]
    index -= 1

# Convert the reversed string back to an integer
reversed_number = int(reversed_number_str)

# Output the reversed number
print(reversed_number)