

# EXERCISE 1: if... elif statements

age = int(input("Enter your age: "))

if age < 13:
        print("Your Discount is: Shs1000")

elif 13 <= age < 18:
    print("Your Discount is: Shs500")

elif 18 <= age < 60:
    print("The price of the movie ticket is: Shs2000")

else:
    print("The price of the movie ticket is: Shs5000")


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

number_str = str(number)

reversed_number_str = ""

length = len(number_str)

# Initialize the index to the last character of the number string
index = length - 1

# Use a while loop to reverse the number string
while index >= 0:
    reversed_number_str += number_str[index]
    index -= 1

# Convert the reversed string back to an integer
reversed_number = int(reversed_number_str)

print(reversed_number)