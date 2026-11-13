# """
# prime_factors(n)
# For an integer n >= 2, return its prime factors in ascending order, repeated by multiplicity. Aim for roughly O(√n) time instead of trying every number up to n.
# prime_factors(60) → [2, 2, 3, 5]
# prime_factors(13) → [13]
# """


# def prime_factors(n):
#     factors = []
#     divisor = 3
#     while divisor * divisor <= n :
#         while n % divisor == 0:
#             n = n // divisor
#             factors.append(divisor)
#         divisor +=2
#     if n > 1:
#         factors.append(n)
#     return factors

# print(prime_factors(60))
# print(prime_factors(13))
# print(prime_factors(23))


def prime_factors(n):
    factors = []
    
    # 1. Pull out all factors of 2 first
    while n % 2 == 0:
        n = n // 2
        factors.append(2)
        print(f"factors = {factors}")

    # 2. Now n is guaranteed to be odd, so we can skip all even divisors!
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            n = n // divisor
            factors.append(divisor)
        divisor += 2
        
    if n > 1:
        factors.append(n)
    return factors

print(prime_factors(60))
print(prime_factors(13))
print(prime_factors(23))