"""
Write a Python program to count and display the vowels of a given text String=”Welcome to python Training
"""
str = "Welcome to python Training"
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vowelsInStr = []
for ch in str:
    if ch in vowels:
        vowelsInStr.append(ch)
print(f"String: {str}")
print(f"Vowels: {vowelsInStr}")
