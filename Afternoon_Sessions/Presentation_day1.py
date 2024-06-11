

# A set is a collection which is unordered, unchangeable*, unindexed, and do not allow duplicate values.
# Set items are unchangeable, but you can remove items and add new items.
# Written using curly braces.

# The values True and 1 are considered the same value in sets, and are treated as duplicates. Duplicate values will be ignored
# The values False and 0 are considered the same value in sets, and are treated as duplicates
# To add an item, we use add() e.g myset.add("hey")
# To remove an item, we use remove() e.g myset.remove("hey").   If the item to remove does not exist, remove() will raise an error.



myset = {"apple", "banana", "cherry"} 
print(myset)

print("apple" in myset)


myset.add("orange")
myset.remove("apple")



# To determine how many items a set has, use the len() function.
print(len(myset))

print(type(myset))



# A set can contain different data types:
set4 = {"abc", 34, True, 40, "male"}
print(set4)

# looping through a set
for x in myset: 
    print(x)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# Both union() and update() will exclude any duplicate items.
# union() returns a new set. e.g set_3 = set_1.union(set_2) or set_3 = set_1 | set_2
set_3 = set1.union(set2)
print(set_3)

# The update() method inserts all items from one set into another and does not return a new set. e.g set_1.update(set_2)
set1.update(set2)
print(set1)

# The intersection() method will return a new set, that only contains the items that are present in both sets. (Keep ONLY the duplicates)
set3 = set1 & set2
print(set3)

# e.g set3 = set1.intersection(set2) or set3 = set1 & set2


# iterators, json, pip

