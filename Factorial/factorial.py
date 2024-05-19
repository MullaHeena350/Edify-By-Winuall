def factorial(n):
    """
    This function calculates the factorial of a given number without using recursion.
    
    Parameters:
    n (int): The number to calculate the factorial of
    
    Returns:
    int: The factorial of the given number
    """
    # Initialize the factorial result to 1
    result = 1
    # Multiply result by each integer from 1 to n
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")  # Output: The factorial of 5 is 120
