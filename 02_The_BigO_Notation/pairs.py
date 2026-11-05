"""
Write a function, pairs, that takes in a list as an argument. The function should return a list containing all unique pairs of elements.

You may return the pairs in any order and the order of elements within a single pair does not matter.

You can assume that the input list contains unique elements.
"""
def pairs(inp:list)-> list[str]:
    new_list = []
    for i in range(0,len(inp)):
        for j in range(i+1,len(inp)):
            pair = [inp[i],inp[j]]
            new_list.append(pair)
            

    return new_list


       

def main():
  
    print(pairs(['a','b']))
    print(pairs(['a','b','c']))
    print(pairs(['a','b','c','a']))
    


if __name__ == "__main__":
    main()    