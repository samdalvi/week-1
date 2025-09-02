

# add code below ...
# Exercise 1: Palindrome Checker
def palindrome(word):
    
    cleaned = word.lower()
    cleaned = cleaned.replace(" ", "")
    cleaned = cleaned.replace(",", "")
    cleaned = cleaned.replace(".", "")
    cleaned = cleaned.replace("!", "")
    cleaned = cleaned.replace("?", "")
    cleaned = cleaned.replace("'", "")
    cleaned = cleaned.replace("-", "")
    
    # Compare string with its reverse
    return cleaned == cleaned[::-1]


# Exercise 2: Parentheses Balance Checker
def parentheses(sequence):
    
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
        status = "✓" if result == expected else "✗"
        print(f"  {status} parentheses('{test}') -> {result}")