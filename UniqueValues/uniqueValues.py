def uniqueValues(arr):
    """
    This function takes an array of integers and returns a new array with only the unique values.
    
    Parameters:
    arr (list): A list of integers
    
    Returns:
    list: A list containing only the unique integers from the input list
    """
    # return list(set(arr))
    unique = []
    for num in arr:
        if num not in unique:
            unique.append(num)
    return unique

inputArray = [5,1, 2, 2, 3, 4, 4, 5,0,0,1,12,]
outputArray = uniqueValues(inputArray)
print(outputArray)
