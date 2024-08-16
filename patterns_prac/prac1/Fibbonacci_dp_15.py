# Calculate the n-th Fibonacci number.
# The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones, starting from 0 and 1.


def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Example Input:
n = 5

# Example Output:
print(fibonacci(n))  # Output: 5
