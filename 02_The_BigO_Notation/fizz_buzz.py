"""
Write a function, fizz_buzz, that takes in a number n as an argument.
The function should return a list containing numbers from 1 to n, replacing certain numbers according to the following rules:

if the number is divisible by 3, make the element "fizz"
if the number is divisible by 5, make the element "buzz"
if the number is divisible by 3 and 5, make the element "fizzbuzz"
"""
## Option 1-- Exclusively do all the calculations
# def fizz_buzz(n):
#     numbers = []
#     for num in range(1,n+1):
#         if num % 3 == 0 and num % 5 == 0:
#             numbers.append("fizzbuzz")
#         elif num % 3 == 0:
#             numbers.append("fizz")
#         elif num %5 ==0:
#             numbers.append("buzz")
#         else :
#             numbers.append(num)
#     return numbers

def fizz_buzz(n:int) -> list[str | int]:
    numbers = []
    for num in range(1, n+1):
        segment = ""
        if num % 3 ==0:
            segment += "fizz"
        if num % 5 == 0:
            segment += "buzz"

        numbers.append(segment if segment else num)
    return numbers



def main():
    usr_input = int(input("Enter the Number: "))
    print(fizz_buzz(usr_input))

if __name__ == "__main__":
    main()