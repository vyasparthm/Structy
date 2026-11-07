"""
custom_fizz_buzz(n, rules)
rules is a list of (divisor, word) pairs. For each number from 1 to n, join the words of every rule whose divisor divides the number, in the order the rules are given.
If no rule applies, keep the number itself. The function should work for any number of rules.
custom_fizz_buzz(10, [(2, "foo"), (3, "bar")]) → [1, "foo", "bar", "foo", 5, "foobar", 7, "foo", "bar", "foo"]
"""
def custom_fizz_buzz(n:int, rules:list[tuple[int,str]])-> list:
    result = []
    for i in range(1, n+1):
        matched_words = [word for divisor,word in rules if i % divisor == 0]
        if matched_words:
            result.append("".join(matched_words))
        else:
            result.append(i)
    return result

print(custom_fizz_buzz(10, [(2, "foo"), (3, "bar"),(4,"bla")]))