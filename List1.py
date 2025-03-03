"""Write a Python program to find duplicate values from a list and display those."""
oldList = [12, 45, 78, 45, 45, "a", "i", "a", "u", "t"]

duplicateList = [i for i in set(oldList) if oldList.count(i) > 1] # add elements those occurrence in list more than one time

print(duplicateList)
