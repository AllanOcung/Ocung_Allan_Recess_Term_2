
#This script talks about error handling in python
#Exception handling with try, except, else and finally
#Custom exceptions

"""
Notes:
Error handling in python helps to handle unexpected situations and errors.
1. Try: contains code that might throw an exception
NB: If an eception occurs, the rest of the code in the try block is skipped or ignored

2. Except: Catches and handles exceptions
NB: You can specify different handlers to different exception types

3.Else: The code runs if no exception occurs
NB: If no exception is raised in the try block, it runs

4. Finally: The code runs whether an exception occurs or not
NB: Used for cleaning up actions

"""
#Example 1: Handle exceptions with division ny zero.
try:
    number = int(input("Enter a number: "))
    result = 20 / number

except ValueError:
    print("Invalid number! please enter a valid number")

except ZeroDivisionError:
    print("Error! Division by zero is not allowed")

else:
    print(f"Result is {result}")

finally:
    print("Excecution completed successfully")

#Exercise 1:
# Write a function that converts a string to an integer and handle both valueError if the string cannot be converted
# to an integer and the TypeError if the input is not a string.
# Use multiple except block to handle these exceptions.

def string_to_integer():
    try:
        convert = input("Enter a string to convert to an integer")
        converted = int(convert)
    except TypeError:
        print("Innput not a string")
    except ValueError:
        print("String can't be converted to an integer")
    else:
        print(f"Converted Integer: {converted}")
    finally:
        print("String converted successfully to an integer")

#Custom exception handling
#Example 2: Exception raised for error in the input, if funds are insufficient.

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {self.amount} with only {self.balance} in account"
        super().__init__(self.message)


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount
    
#Custom exception handling
try:
    balance = 20000
    amount_to_withdraw = 100000
    new_balance = withdraw(balance, amount_to_withdraw)

except InsufficientFundsError as e:
    print("Error: {e.message}")

else:
    print(f"withdrawal successfully! New balance is {new_balance}")

finally:
    print("Transaction completed")

"""
Note:
Defining a custom Exception
class CustomError(Exception):
# Custom exception for specific error cases

def __init__(self, message):
     super().__init__(message)
     self.message = message

#Raising a custom exception
def check_value(vaue):
    if value is < 0 or value:
        raise CustomError("Value cannot be negative")
    return value

#Handle exception with try block error

"""
#Exercise 2:
#Create a custom exception InvalidAgeError and write a function that raises this exception if the given age
#is negative. Handle this custom exception when calling the function

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age =age
        self.message = f"{age} can not be negative"
        super().__init__(self.message)

def determine_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    return age

try:
    age = int(input("Enter your age"))
    determine_age(age)
except InvalidAgeError:
    print("Age cannot be negative")
else:
    print(f"Age is: {age}")
finally:
    print("Execution complete")
