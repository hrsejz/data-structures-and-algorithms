def fibonacci(n):
    """
    Recursive function to calculate the Fibonacci number at position 'n'.
    The Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1."""

    # Ensure that the input 'n' is a non-negative integer.
    assert n >= 0 and int(n) == n, "Input must be a non-negative integer."

    # Base case: Fibonacci of 0 is 0.
    if n == 0:
        return 0
    # Base case: Fibonacci of 1 is 1.
    elif n == 1:
        return 1
    # Recursive case: Fibonacci of n is the sum of Fibonacci of (n-1) and (n-2).
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Prompt the user to input a number for the Fibonacci sequence.
n = int(input("Enter a non-negative integer to find its Fibonacci value: "))
# Calculate the Fibonacci number at the input position.
result = fibonacci(n)
# Display the result.
print(f"The Fibonacci number at position {n} is {result}.")
