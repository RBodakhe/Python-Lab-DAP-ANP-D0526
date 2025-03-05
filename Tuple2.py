"""
Write a Python program to calculate the sum of the numbers in a given tuple.
Input: tuples_list = [(1, 2), (3, 4), (5, 6)]
"""

tuples_list = [(1, 2), (3, 4), (5, 6)]
counter = 1
for tup in tuples_list:
    print(f"{counter}. Sum of tuple{tup} is {sum(tup)}")
    counter += 1
