"""
Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.
"""
import numpy as np

# Create the array of 10 zeros, 10 ones, and 10 fives
arr_zeros_ones_fives = np.array([0]*10 # for implicating 10 zero elements
                       + [1]*10 # for implicating 10 one elements
                       + [5]*10) # for implicating 10 five elements

# reshaping for better appearance
arr_zeros_ones_fives=arr_zeros_ones_fives.reshape(6,-1)

# printing the array
print("Final Array:")
print(arr_zeros_ones_fives)