from fizz_buzz import fizz_buzz

def test_fizzbuzz():
    assert fizz_buzz(10) == [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz']
    assert fizz_buzz(15) == [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz']
    print("All tests passed")

test_fizzbuzz()    