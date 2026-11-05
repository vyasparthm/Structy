"""
Write a function, is_prime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.
"""
def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2,n):
        if n % divisor == 0:
            return False
    return True
       
def main():
    inp = int(input("Enter Number: "))
    print(is_prime(inp))

if __name__ == "__main__":
    main()

        