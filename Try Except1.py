"""
Write a Python program that prompts the user to input an integer and
raises a ValueError exception if the input is not a valid integer.
"""

try:
    # Prompting user input
    number = int(input("Enter an integer: "))
    print(f"You entered {number}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")  # User-friendly message
