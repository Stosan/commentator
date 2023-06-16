def detect_programming_language(function: str) -> str:
    # Convert the function to lowercase for case-insensitive comparison
    function = function.lower()

    if function[:3] == "def":
        return "Python"
    elif function[:4] == "func":
        return "Go"
    elif function[:8] == "function":
        return "JavaScript"

    return "Unknown"
