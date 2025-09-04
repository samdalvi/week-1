# Exercise 1: Palindrome Checker
def palindrome(word):
    """
    Check if a word or phrase is a palindrome (reads the same forwards and backwards).
    
    Parameters:
    word (str): The string to check for palindrome property
    
    Returns:
    bool: True if the string is a palindrome, False otherwise
    """
    cleaned = word.lower()
    
    remove_chars = [" ", ",", ".", "!", "?", "'", "-"]
    for char in remove_chars:
        cleaned = cleaned.replace(char, "")
    
    # Compare string with its reverse
    return cleaned == cleaned[::-1]

# Exercise 2: Parentheses Balance Checker
def parentheses(sequence):
    """
    Check if parentheses in a string are properly balanced.
    
    Parameters:
    sequence (str): The string containing parentheses to check
    
    Returns:
    bool: True if parentheses are balanced, False otherwise
    """
    balance = 0
    
    for char in sequence:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False
    
    return balance == 0

# Test the functions
if __name__ == "__main__":
    print("\n EXERCISE 1: Palindrome Tests ")
    palindrome_tests = [
        "racecar",
        "Nurses Run", 
        "Sit on a potato pan, Otis."
    ]
    
    for test in palindrome_tests:
        result = palindrome(test)
        print(f"palindrome('{test}') -> {result}")
    
    print("\n EXERCISE 2: Parentheses Balance ")
    parentheses_tests = [
        ("((blah)()()())", True),
        ("(((())blee))", True),
        ("(()hello((())()))", True),
        ("((((((())", False),
        ("()))", False)
    ]
    
    for test, expected in parentheses_tests:
        result = parentheses(test)
        print(f"  parentheses('{test}') -> {result}")

