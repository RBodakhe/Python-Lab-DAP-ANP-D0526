"""Write a Python program to Get Only unique items from two sets.

Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70}

Output: {70, 40, 10, 50, 20, 60, 30}"""

setA = {10, 20, 30, 40, 50}
setB = {30, 40, 50, 60, 70}
setAUnionSetB = setA.union(setB)

print(f"A = {setA}")
print(f"B = {setB}")
print(f"A U B ={setAUnionSetB}")
