"""
Take a list of names and return one string with a "hey <name>" greeting for each, separated by ", ".
greet_all(["Ann", "Bo"]) → "hey Ann, hey Bo"
"""

def greet_all(names:list)->str:
    greetings = (f"Hey {name}" for name in names)
    return ",".join(greetings)

print(greet_all(["Ann", "Bo"]))