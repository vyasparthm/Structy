"""
Write a function, pairs, that takes in a list as an argument. The function should return a list containing all unique pairs of elements.

You may return the pairs in any order and the order of elements within a single pair does not matter.

You can assume that the input list contains unique elements.
"""
def pairs(inp:list)-> list[str]:
    new_list = []
    for item in inp[:-1]:
        for item in inp[1:]:
            if item != item +1:
                new_list.append(item,)
    return new_list

def main():
    a = input("enter list: ")
    print(pairs(a))


if __name__ == "__main__":
    main()    