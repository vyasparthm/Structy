"""
Return the length of the longest streak of consecutive even numbers in the list. Return 0 if there are none.
longest_even_run([2, 4, 1, 6, 8, 10, 3]) → 3
longest_even_run([1, 3, 5]) → 0
"""


def longest_even_run(nums:list):
    
    current_streak = 0
    max_streak = 0
    for num in nums:
       if num % 2 == 0:
           current_streak += 1
           max_streak = max(max_streak,current_streak)
       else: 
           current_streak = 0
    
            
    return max_streak




print(longest_even_run([2,4,5,8,10,11,12,14,16,18,19]))
