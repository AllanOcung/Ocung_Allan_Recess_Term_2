
'''
In Python, arrays can be managed using several data structures, the most common being lists, 
NumPy arrays, and arrays from the array module. Below, I'll cover the basics of each.

Lists
Python lists are flexible and can hold items of different types. They are widely used 
due to their built-in functionalities.

Creating and using lists

'''

my_list = [1, 2, 3, 4, 5]

print(my_list[0])  # Output: 1

my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

my_list.pop(0)
print(my_list)  # Output: [2, 3, 4, 5, 6]


'''
Array Module
The array module provides an array type that is more space-efficient 
than lists, but it only supports arrays of basic data types.

'''

import array as arr

my_array = arr.array('i', [1, 3, 5, 7, 9]) # 'i' indicates an array of integers

print(my_array[1])

my_array[0] = 17

print(my_array[0])

my_array.append(11)

print(my_array)

my_array.pop(1)

print(my_array)