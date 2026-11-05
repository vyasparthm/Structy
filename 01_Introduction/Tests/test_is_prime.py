import pytest
from is_prime import is_prime

@pytest.mark.parametrize(
    "n,expected",
[
    # Non negative
    (-5, False),
    (0,False),
    #Smallest Prime
    (2,True),
    
    #Small primes
    (3,True),
    (5,True),
    (7,True),
    # Small composite numbers (even & odd)
    (4, False),
    (6, False),
    (9, False),  # 3 * 3 (catches code checking only even divisors)
    (15, False),  # 3 * 5
    # Larger numbers
    (29, True),
    (100, False),
])
def test_is_prime(n:int, expected:bool):
    assert is_prime(n) == expected