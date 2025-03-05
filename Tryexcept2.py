"""
Write a Python program that opens a file and handles a FileNotFoundError
exception if the file does not exist.
"""

file_name = "sample.txt"  # File name to open

try:
    with open(file_name, "r") as my_file:  # Using 'with' to ensure proper file handling
        print(my_file.read())  # Reading and printing file content
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")  # Improved error message
