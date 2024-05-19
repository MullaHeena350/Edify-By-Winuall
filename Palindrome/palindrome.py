def isPalindrome(s):
    """
    Check if a given string is a palindrome.
    
    Parameters:
    s (str): The string to check
    
    Returns:
    bool: True if the string is a palindrome, False otherwise
    """
    # s = s.lower().replace(" ", "")
    # return s == s[::-1]
    s = s.lower().replace(" ", "")
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

testString = "A man a plan a canal Panama"
if isPalindrome(testString):
    print("Yes the given string is a palindrome")
else:
    print("No the given string is not a palindrome")
