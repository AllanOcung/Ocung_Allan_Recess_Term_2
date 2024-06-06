# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.


# 1.	Create a list with 5 items (names of people) and write a python program to output the 2nd item.

mylist = ["Moses", "Albert", "Andrew", "Ocung", "Mark", "John"]

print(mylist[1])

# 2.	Write a python program to change the value of the first item to a new value

mylist[0] = "Allan"

print(mylist[0])

# 3.	Write a python program to add a sixth item to the list

mylist.insert(5, "Joviah")

print(mylist)

# 4.	Write a python program to add “Bathel” as the 3rd item in your list

mylist.insert(2, "Bathel")

print(mylist)

# 5.	Write a python program to remove the 4th item from the list

mylist.pop(3)

print(mylist)

# 6.	Use negative indexing to print the last item in your list

print(mylist[-1])

# 7.	Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.

mylist2 = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

print(mylist2[2:5])

# 8.	Write a list of countries and make a copy of it.

african_countries = ["Nigeria", "Kenya", "South Africa", "Egypt", "Ghana"]

african_countries_copy = african_countries.copy()

print("Original list:", african_countries)
print("Copied list:", african_countries_copy)

# 9.	Write a python program to loop through the list of countries

for x in african_countries:
    print(x)

# 10.	Write a list of animal names and sort them in both descending and ascending order.

wild_animals = ["Lion", "Tiger", "Elephant", "Giraffe", "Zebra"]

wild_animals_ascending = sorted(wild_animals)

print("Ascending Order: ", wild_animals_ascending)

wild_animals_descending = sorted(wild_animals, reverse=True)

print("Descending Order: ", wild_animals_descending)

# 11.	Using the list above, write a python program to output only animal names with the letter ‘a’ in them

new_wild_animals = [x for x in wild_animals if "a" in x]

print(new_wild_animals)

# 12.	Write two lists, one containing your first names and the other your second names. Join the two lists.

first_names = ["Allan", "Francis"]

second_names = ["Ocung", "Tabo"]

first_names.extend(second_names)

print(first_names)

