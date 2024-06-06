# 1.	Use the set() constructor to create a set of 3 of your favorite beverages.

myBeverages = set(("coffe", "Orange juice", "Green tea"))

print(myBeverages)

# 2.	Use the correct method to add 2 more items to the beverages set.

myBeverages.add("Soda")

myBeverages.add("Smoothie")

print(myBeverages)

# 3.	Given the set below;
# mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
# Check if microwave is present in the set.

myset = {"oven", "kettle", "microwave", "refrigerator"}

print("microwave" in myset)

# 4.	Write a python program to remove “kettle” from the set above.

myset.remove("kettle")

print(myset)

# 5.	Write a python program to loop through the set above.

for x in myset:
    print(x)

# 6.	Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.

mySet = {'apple', 'banana', 'cherry', 'date'}

mylist = ['elderberry', 'fig']

mySet.update(mylist)

print(mySet)

# 7.	Write two sets, one containing your ages and the other your first names. Join the two sets.

ages = {25, 30, 35}

first_names = {"Alice", "Bob", "Charlie"}

combined_set = ages.union(first_names)

print(combined_set)
