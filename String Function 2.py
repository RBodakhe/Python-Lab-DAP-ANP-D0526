"""Write a Python program to remove duplicate words of a given string.

Input = “String and String Function”

Output: String and Function"""

str1 = input("Enter a String:\n")
wordSet = set()  # set is a collection of unique value

for word in str1.split(" "):
    wordSet.add(word)  # duplicate values are not considered in a set
    # so duplicate values are not stored in wordSet

print("After removing duplicate words the String")
print(" ".join(wordSet))
