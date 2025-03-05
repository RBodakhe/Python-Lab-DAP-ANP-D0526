"""
Write a Python program to Count all letters, digits, and special symbols from the given string 

Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 2 Symbol = 3
"""
str1 = input("Enter a string to calculate Alphabets, Digits, and Symbols present in the String:\n")
alphaCount = 0
digitCount = 0
symbolCount = 0

for ch in str1:
    if ch.isalpha():
        alphaCount += 1
    elif ch.isdigit():
        digitCount += 1
    else:
        symbolCount += 1
print(f"Your String: {str1}")
print(f"Number of Alphabets: {alphaCount}")
print(f"Number of Digits: {digitCount}")
print(f"Number of Symbols: {symbolCount}")
