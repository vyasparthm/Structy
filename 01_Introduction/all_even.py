"""
Write a function, all_even, that takes in a list of numbers as an argument. 
The function should return a boolean indicating whether or not every element of the list is an even number.

You can assume that the list is non-empty.
"""
## Simple implementation
# def all_even(nums):
#     for num in nums:
#         if num % 2 != 0:
#             return False
#     return True

def all_even(nums):
    return all(num % 2 ==0 for num in nums)