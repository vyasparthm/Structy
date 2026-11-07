"""
fizz_buzz_count(n)
Return how many numbers from 1 to n (inclusive) are divisible by 3 or 5 (or both).
fizz_buzz_count(15) → 7 (3, 5, 6, 9, 10, 12, 15)
"""
def fizz_buzz_count(n:int):
    div_both = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            div_both += 1
        elif i % 5 == 0:
            div_both += 1
        
    return div_both


print (fizz_buzz_count(15))