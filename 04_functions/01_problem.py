#  Problem: Write a function to calculate and return the square of a number.

def square(num):
    """
    This function takes a number as input and returns its square.
    
    Parameters:
    num (int or float): The number to be squared.
    
    Returns:
    int or float: The square of the input number.
    """
    return num ** 2

result = square(5)
print(f"The square of 5 is: {result}")