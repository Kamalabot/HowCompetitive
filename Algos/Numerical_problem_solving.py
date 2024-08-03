""" Root-Finding with Newton's Method:

Newton's method is used to find the roots (or zeros) of a real-valued function. It's commonly employed in various fields, including engineering and physics. Let's use Newton's method to find the square root of a number:
 """
def newton_sqrt(number, epsilon=1e-6, max_iterations=100):
    guess = number / 2.0  # Initial guess
    for _ in range(max_iterations):
        guess = 0.5 * (guess + number / guess)  # Update the guess
        if abs(guess * guess - number) < epsilon:  # Check for convergence
            return guess
    raise ValueError("Newton's method did not converge")

# Example usage:
number = 25.0
sqrt_estimate = newton_sqrt(number)
print(f"Estimated square root of {number} is approximately {sqrt_estimate:.6f}")

""" Numerical Integration with the Trapezoidal Rule:

The trapezoidal rule is used to approximate the definite integral of a function. It has applications in physics, engineering, and economics. Here's an implementation to estimate the integral of a function:
 """
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    result = 0.5 * (func(a) + func(b))  # First and last terms
    for i in range(1, n):
        result += func(a + i * h)
    return result * h

# Example usage: Estimate the integral of f(x) = x^2 from 0 to 1
def func(x):
    return x ** 2

a, b = 0, 1  # Integration limits
n = 1000     # Number of intervals
integral_estimate = trapezoidal_rule(func, a, b, n)
print(f"Estimated integral: {integral_estimate:.6f}")
""" Linear Regression with Gradient Descent:

Linear regression is a fundamental technique in machine learning and statistics used for modeling relationships between variables. Gradient descent is used to find the coefficients of the linear model. Here's an example of linear regression using gradient descent:
 """
import numpy as np

def gradient_descent(X, y, learning_rate=0.01, epochs=1000):
    m, n = X.shape
    theta = np.zeros(n)
    for _ in range(epochs):
        predictions = X.dot(theta)
        errors = predictions - y
        gradient = (1 / m) * X.T.dot(errors)
        theta -= learning_rate * gradient
    return theta

# Example usage: Linear regression on a toy dataset
X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
theta = gradient_descent(X, y)
print(f"Linear regression coefficients: {theta}")