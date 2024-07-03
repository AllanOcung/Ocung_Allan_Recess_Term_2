# 1.	Declare two variables, an integer and a string and use the correct method to concatenate the two variables.

number = 14
text = "Number: "

result = "{} {}".format(text, number)

print(result)

# 2.	Consider the example below;
# txt = “      Hello,       Uganda!       ”
# Output the string without spaces at the beginning, in the middle and at the end.

txt = "      Hello,       Uganda!       "

trimmed_txt = txt.strip() # Remove spaces from the beginning and the end

new_txt = " ".join(trimmed_txt.split()) # Remove spaces in the middle

print(new_txt)

# 3.	Write a python program to convert the value of ‘txt’ to uppercase.

txt = "Hello, Uganda!"

txt_to_uppercase = txt.upper()

print(txt_to_uppercase)

# 4.	Write a python program to replace character ‘U’ with ‘V’ in the string above.

modifieded_txt = txt.replace('U', 'V')

print(modifieded_txt)

# 5.	Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.
# y = “I am proudly Ugandan”

y = "I am proudly Ugandan"

substring = y[1:4]

print(substring)

# 6.	The piece of code below will give an error when output;
# x = “All “Data Scientists” are cool!” 
# Write a python program to correct it.

x = 'All "Data Scientists" are cool!'

print(x)

