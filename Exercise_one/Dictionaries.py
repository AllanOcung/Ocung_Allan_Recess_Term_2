# 1.	With reference to the dictionary below, write a python program to print the value of the shoe size. 
#   Add this dictionary to your .py file
#   Shoes = {
# 	    “brand” : “Nick”,
# 	    “color” : “black”,
# 	    “size” : 40
# 	    }

shoes = {
    "brand" : "Nick",
    "color" : "black",
    "size" : 40
    }

print(shoes["size"])

# 2.	Write a python program to change the value “Nick” to “Adidas”

shoes["brand"] = "Adidas"

print(shoes)

# 3.	Write a python program to add a key/value pair "type”: "sneakers" to the dictionary

shoes["type"] = "sneakers"

print(shoes)

# 4.	Write a python program to return a list of all the keys in the dictionary above.

keys = shoes.keys()

print(keys)


# 5.	Write a python program to return a list of all the values in the dictionary above.

values = shoes.values()

print(values)

# 6.	Check if the key “size” exists in the dictionary above.

if "size" in shoes:
    print("Yes, 'size' is one of the keys in the shoes dictionary")

# 7.	Write a python program to loop through the dictionary above.

for x in shoes:
    print(x)

# 8.	Write a python program to remove “color” from the dictionary.

shoes.pop("color")

print(shoes)

# 9.	Write a python program to empty the dictionary above.

shoes.clear()

print(shoes)

# 10.	Write a dictionary of your choice and make a copy of it.

dict_origin = {
    'name': 'Alonzo',
    'age': 24,
    'occupation': 'Engineer',
    'city': 'Soroti'
}

coped_dict = dict_origin.copy()

print(coped_dict)

# 11.	Write a python program to show nested dictionaries

myfamily = {
  "first_child" : {
    "name" : "Emily",
    "year" : 2001
  },
  "second-child" : {
    "name" : "Toby",
    "year" : 2003
  },
  "third_child" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])