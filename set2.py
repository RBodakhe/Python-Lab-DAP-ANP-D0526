"""Write a Python program to Remove items from set1 that are not common to both set1 and set2.

Input: set1 = {10, 20, 30, 40, 50}

set2 = {30, 40, 50, 60, 70}

Output: {40, 50, 30}"""

setA = {10, 20, 30, 40, 50}

setB = {30, 40, 50, 60, 70}
print(f"A = {setA}")
print(f"B = {setB}")
setAIntersectionSetB = setA.intersection(setB)
for i in setAIntersectionSetB:
    setA.remove(i)
print("After remove items from setA that are not common to both setA and setB.")
print(f"A = {setA}")
