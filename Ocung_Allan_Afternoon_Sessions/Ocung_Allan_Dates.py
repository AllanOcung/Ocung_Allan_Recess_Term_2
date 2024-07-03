
# Python Dates

'''
A date in Python is not a data type of its own, but we can import 
a module named datetime to work with dates as date objects.

'''

# Import the datetime module and display the current date:

from datetime import datetime, date, time, timedelta

x = datetime.now() # The date contains year, month, day, hour, minute, second, and microsecond.

# print(x)

'''
The datetime module has many methods to return information about the date object.
'''

# Return the year and name of weekday
print(x.year)

print(x.strftime("%A"))


# Creating Date Objects

'''
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.

'''

now = datetime.now() # Current date and time

print(f"Now: {now}")

today = date.today() # Current date

print(f"Today: {today}")

# Format current date and time
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Now:", formatted_now)

