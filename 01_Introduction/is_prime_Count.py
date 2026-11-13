"""
count_primes_up_to(n)
Return how many prime numbers are less than or equal to n.
count_primes_up_to(10) → 4 (2, 3, 5, 7)
count_primes_up_to(1) → 0
"""


def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2,int(n** 0.5)+1):
        if n % divisor == 0:
            return False
    return True

def count_primes_up_to(n):
    occurance = 0
    for number in range(2,n+1):
        if  is_prime(number) == True:
            occurance +=1
    return occurance

print(count_primes_up_to(7))
     