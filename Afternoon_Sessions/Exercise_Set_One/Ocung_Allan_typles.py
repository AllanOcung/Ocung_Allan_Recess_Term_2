# 1.	Consider the tuple below;
# x = (“samsung”, “iphone”, “tecno”, “redmi”)
# 	Write a python program to output your favorite phone brand.

x = ("samsung", "iphone", "tecno", "redmi")

print("My favorite phone brand is: ", x[0])

# 2.	Use negative indexing to print the 2nd last item in your tuple. 

print(x[-2])

# 3.	Using the phones list above, write a python program to update “iphone” to “itel”

# convert the tuple into a list, change the list, and convert the list back into a tuple.
y = list(x)

y[1] = "itel"

x = tuple(y)

print(x)

# 4.	Write a python program to add “Huawei” to your tuple.

y = list(x)

y.append("Huawei")

x = tuple(y)

print(x)

# 5.	Write a python program to loop through the tuple above.

for phone in x:
    print(phone)

# 6.	Write a python program to remove/delete the first item in your tuple.
y = list(x)

y.remove("samsung")

x = tuple(y)

print(x)


# 7.	Using the tuple() constructor, create a tuple of the cities in Uganda.

ugandan_cities = tuple(("Kampala", "Entebbe", "Soroti", "Mbale"))

print(ugandan_cities)

# 8.	Write a python program to unpack your tuple.

(capital_city, island, sun_city, eastern_Ug) = ugandan_cities

print(capital_city, island, sun_city, eastern_Ug)

# 9.	Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.

print("The 2nd, 3rd, and 4th cities are:", ugandan_cities[1:4])

# 10.	Write two tuples, one containing your first names and the other your second names. Join the two tuples.

first_names = ("Allan", "Bob", "Charlie")

second_names = ("Ocung", "Jones", "Brown")

full_name = first_names + second_names

print(full_name)

# 11.	Create a tuple of colors and multiply it by 3.

colors = ("red", "blue", "green")

multiplied_colors = colors * 3

print(multiplied_colors)

# 12.	Return the number of times 8 appears in this tuple

number_tuple = (1, 3, 7, 1, 7, 5, 4, 6, 1, 5)

count_of_1 = number_tuple.count(1)

print(f"The number 1 appears {count_of_1} times in the tuple.")