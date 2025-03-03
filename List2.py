"""Write a Python program to get the largest and smallest number from a list without builtin functions."""
import random

nums = [random.randint(10, 99) for _ in range(10)]  # creates 10 random numbers between 10 and 99
maxNum = nums[0]
minNum = nums[0]
for num in nums:
    if maxNum < num:
        maxNum = num  # Update the value of maxNum if it is less than current num

    if minNum > num:
        minNum = num  # Update the value of minNum if it is greater than current num
print(f"Number List: {nums}")
print(f"Largest No: {maxNum}")
print(f"Smallest No: {minNum}")
