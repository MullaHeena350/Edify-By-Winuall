def factorial(n):
    """
    Recursive function to calculate the factorial of a number.

    The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
    It is denoted by n! and is defined as:
    - n! = n * (n-1) * (n-2) * ... * 1
    - By convention, 0! is defined to be 1.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number n.

    Raises:
    ValueError: If n is a negative integer.

    Example:
    >>> factorial(5)
    120

    Explanation:
    The factorial of 5 (5!) is calculated as:
    5! = 5 * 4 * 3 * 2 * 1 = 120
    """
    # Check if n is a negative integer
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers")
    
    # Base case: if n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage
number = 8
print(f"The factorial of {number} is {factorial(number)}")
