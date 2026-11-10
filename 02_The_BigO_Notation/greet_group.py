"""
greet_group(names)
Return a single natural-sounding greeting for a group:

0 names → "hey everyone"
1 name → "hey Ann"
2 names → "hey Ann and Bo"
3 or more → "hey Ann, Bo, and Cy" (with the Oxford comma)
"""

def greet_group(names:list)-> str:
    if len(names)== 0:
        return "hey everyone"
    elif len(names)>= 2:
            greetings = (f"hey {name}" for name in names[:-1])
            All_minusOne= ",".join(greetings)
            return f"{All_minusOne}, and hey {names[-1]}"



# print(greet_group(["Ann", "Bo","Joe"]))    
print(greet_group(["Ann", "Bo"]))
# print(greet_group([]))    
