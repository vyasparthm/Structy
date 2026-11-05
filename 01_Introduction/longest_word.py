"""Write a function, longest_word, that takes in a sentence string as an argument. The function should return the longest word in the sentence. If there is a tie, return the word that occurs later in the sentence.

You can assume that the sentence is non-empty."""

def longest_word(sentence):
    broken = sentence.split(" ")
    longest = broken[0]
    for word in broken[1:]:
        if len(word) >= len(longest):
            longest = word
    return longest


def main():
    a = input("What is the sentence? ")
    print(longest_word(a))

if __name__ == "__main__":
    main()