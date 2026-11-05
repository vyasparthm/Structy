"""
Take a non-empty list of integers and an integer k. Return True if every element is divisible by k, otherwise False.
all_divisible([6, 12, 18], 3) → True
all_divisible([6, 12, 19], 3) → False
"""

def all_divisible(nums:list,k:int):
    return all(num % k ==0 for num in nums)
