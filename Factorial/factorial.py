def factorial(n):
    """
    This function calculates the factorial of a given non-negative integer without using recursion.
    
    Parameters:
    n (int): The number to calculate the factorial of
    
    Returns:
    int: The factorial of the given number, or -1 if n is negative
    """
    if n < 0:
        return -1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage:
number = 5
result = factorial(number)
if result == -1:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is {result}")
