#Let’s write a Python program to calculate the factorial of a given number. 
#The factorial of a non-negative integer n (denoted as n!) is the product of all positive integers from 1 to n.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Lets try the above example with while loop
def while_factorial(n):
    result = 1
    i=1
    while i <= n:
        result *= i
        i += 1
    return result


# Example usage:
number = int(input("Enter the number to calculate factorial: "))
print(f"The factorial of {number} using for loop is {while_factorial(number)} ")
print(f"The factorial of {number} using while loop is {factorial(number)}")


