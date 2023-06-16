import re

def detect_programming_language(function: str) -> str:
    # Convert the function to lowercase for case-insensitive comparison
    function = function.lower()

    if re.search(r"^async\s+function", function):
        return "JavaScript"
    elif re.search(r"^function", function):
        return "JavaScript"
    elif re.search(r"^def", function):
        return "Python"
    elif re.search(r"^async\s+def", function):
        return "Python"
    elif re.search(r"^\s*go\s+func", function):
        return "Go"
    elif re.search(r"^func", function):
        return "Go"
    

    return "Unknown"
